#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

require './dataroot/index1.cgi';
require './dataroot/index2.cgi';

if($MENTE) { &ERR2("ũƮ üũ  Ͻ մϴ."); }
&DECODE;

# -------------------------------------------------------------------------
# ADMIN TURN FORCE (added)
# - Allows admin to force-run N turns (1..30) from the admin panel.
# - Params: turn_force=1, turn_n=1..30, id/pass = admin credentials.
# -------------------------------------------------------------------------
our $FORCE_TURN_N = 0;
our $FORCE_ADMIN_OK = 0;
our $FORCE_STOP_ELIM = 0;
our $FORCE_STOP_CID = 0;
if (defined $FORM{'turn_force'} && $FORM{'turn_force'} eq '1') {
    my $aid = $FORM{'id'} || '';
    my $apw = $FORM{'pass'} || '';
    if ($aid eq 'pwh857' && $apw eq '921002') {
        $FORCE_ADMIN_OK = 1;
        my $n = $FORM{'turn_n'}; $n =~ s/[^0-9]//g;
        $n = int($n||0);
        if ($n < 1) { $n = 1; }
        if ($n > 30) { $n = 30; }
        $FORCE_TURN_N = $n;
        $FORCE_STOP_ELIM = (defined $FORM{'stop_elim'} && $FORM{'stop_elim'} eq '1') ? 1 : 0;
        my $sc = $FORM{'stop_cid'}; $sc =~ s/[^0-9]//g; $FORCE_STOP_CID = int($sc||0);
    }
}

# -------------------------------------------------------------------------
# FORCE STOP CONDITION (added)
# - stop_elim=1 and stop_cid=N: stop forced loop when country N is eliminated
# - elimination = no towns owned + no characters in that country
# -------------------------------------------------------------------------
sub FORCE_CHECK_ELIM {
    my ($cid) = @_;
    $cid = int($cid||0);
    return 0 if ($cid <= 0);

    my $towns = 0;
    if (open(my $TF, "./log_file/f_town_data.cgi")) {
        while(my $l = <$TF>) {
            chomp($l);
            next if ($l eq '');
            my @p = split(/<>/, $l);
            my $owner = int($p[16]||0);
            if ($owner == $cid) { $towns++; }
        }
        close($TF);
    }

    my $chars = 0;
    my $mdir = "./charalog/main";
    if (-d $mdir) {
        opendir(my $DH, $mdir);
        my @ff = readdir($DH);
        closedir($DH);
        foreach my $f (@ff) {
            next unless ($f =~ /\.cgi$/);
            my $path = "$mdir/$f";
            next unless (-f $path);
            if (open(my $CF, $path)) {
                my $ln = <$CF>;
                close($CF);
                next unless defined $ln;
                my @b = split(/<>/, $ln, -1);
                my $c = int($b[2]||0);
                if ($c == $cid) { $chars++; }
            }
        }
    }

    return (($towns <= 0) && ($chars <= 0)) ? 1 : 0;
}

&TOP;
&COUNTRY_DATA_OPEN("$kcon");
&CHARA_MAIN_OPEN; 

sub TOP {

	# -------------------------------------------------------------
	# TOP FORCE LOOP (added)
	# - If admin requested turn_force, run TOP multiple times.
	# - We don't remove any existing turn checks; instead we
	#   temporarily bump $date so the existing update path triggers.
	# -------------------------------------------------------------
	TOP_FORCE_REDO:

	$date = time();
	$month_read = "./log_file/date_count\.cgi";
	open(IN,"$month_read") or &ERR2('  ʾҽϴ.');
	@MONTH_DATA = <IN>;
	close(IN);

    # []  Ľ ǹ üũ  ̵ ( ߿)
	($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
	# Ensure update path triggers when forced
	if ($FORCE_ADMIN_OK && $FORCE_TURN_N > 0) {
		$date = $mtime + $TIME_REMAKE + 1;
	}

	&TIME_DATA;

    # [ ڵȭ] ǽð Ȯ   ȣ ϵ,  Ʈ ($is_update) 
	my $is_update = ($mtime + $TIME_REMAKE < $date) ? 1 : 0;
	if ($FORCE_ADMIN_OK && $FORCE_TURN_N > 0) { $is_update = 1; }
	if ($FORCE_ADMIN_OK && $FORCE_TURN_N > 0) { $is_update = 1; }
    &BOT_PROCESS($is_update);

	# --- TURN FORCE LOG (added) ---
	if ($FORCE_ADMIN_OK && $FORCE_TURN_N > 0) {
		my $lf = "./log_file/turn_force.log";
		if (open(my $LF, ">>$lf")) {
			eval { flock($LF, 2); };
			my $ts = time();
			print $LF "$ts<>ADMIN_FORCE<>$FORM{'id'}<>left=$FORCE_TURN_N<>\n";
			close($LF);
			chmod(0666, $lf);
		}
	}

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<12){$S_MES .= "&nbsp;$S_MOVE[$p]<BR>";$p++;}

	open(IN,"$MAP_LOG_LIST2");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<11){$D_MES .= "&nbsp;$S_MOVE[$p]<BR>";$p++;}

	open(IN,"$MAP_LOG_LIST3");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<4){$G_MES .= "&nbsp;$S_MOVE[$p]<BR>";$p++;}

	$hit = 0;
	@month_new=();

    # Ʒ   ý۰ ȣȯ  
	$old_date = sprintf("%02d\%02d\", $F_YEAR+$myear, $mmonth);

	if($ACT_LOG){
		$actfile = "./log_file/act_log.cgi";
		open(IN, "<", $actfile) or die "cannot open $actfile";
		@ACT_DATA = <IN>;
		close(IN);
		($qsec,$qmin,$qhour,$qday) = localtime($date);
		$p=0;
		while($p<5){$A_MES .= "<font color=880000></font>$ACT_DATA[$p]<BR>";$p++;}

		$ACT_MES = "<TR><TD bgcolor=#EFE0C0 colspan=\"0\" width=80% height=20><font color=#8E4C28 size=2>$A_MES</font></TD></TR>";

	}

	open(IN,"$DEF_LIST") or &ERR("   ʽϴ.");
	@DEF_DATA = <IN>;
	close(IN);

	open(IN,"$TRAP_LIST");
	@TRAP_DATA = <IN>;
	close(IN);

	open(IN,"$TOWN_LIST") or &ERR("   ʽϴ.");
	@TOWN_DATA = <IN>;
	close(IN);
	($zwname,$wzc)=split(/<>/,$TOWN_DATA[0]);
	$zzhit=0;
	foreach(@TOWN_DATA){
		($zwname,$zwcon)=split(/<>/);
			if($wzc ne $zwcon){$zzhit=1;}
			$wzc = $zwcon;
	}

	&CHEACK_COM;
	if($mtime + $TIME_REMAKE < $date){
        
		if($mtime eq ""){
		$mtime = $date;
		&MAP_LOG(" ߽ϴ.");
		}else{
		$mtime += $TIME_REMAKE;
		}
		$mmonth++;
		if($mmonth > 12){
			$myear++;
			$mmonth=1;
		}
		unshift(@month_new,"$myear<>$mmonth<>$mtime<>\n");
		if($ACT_LOG){
			($qsec,$qmin,$qhour,$qday) = localtime($mtime);
			unshift(@ACT_DATA,"===============[$myear$mmonth]=================\n");
		}

		open(IN,"$COUNTRY_LIST") or &ERR2('  ʾҽϴ. err no :country');
		@COU_DATA = <IN>;
		close(IN);
		@NEW_COU_DATA=();
		foreach(@COU_DATA){
			($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri,$xvch)=split(/<>/);
			$xvmark++;
			push(@NEW_COU_DATA,"$xvcid<>$xvname<>$xvele<>$xvmark<>$xvking<>$xvmes<>$xvsub<>$xvpri<>$xvch<>\n");
		}
		open(OUT,">$COUNTRY_LIST") or &ERR('COUNTRY ͸   ϴ.');
		print OUT @NEW_COU_DATA;
		close(OUT);

	if($go_ex < 500000){
		$sangtae = "ǰ";
	}elsif($go_ex <500000 && $go_ex > 500001){
		$sangtae = "";
	}elsif($go_ex < 500001 && $go_ex > 500002){
		$sangtae = "";
	}elsif($go_ex < 500002 && $go_ex > 500003){
		$sangtae = "";
	}elsif($go_ex <500003 && $go_ex > 500004){
		$sangtae = "";
	}

		$b_hit = 0;
		if($mmonth eq "1"){
			&MAP_LOG("<img src=$IMG/j11.gif> <font color=orange></font> Ȱ ϵ�  ?�Ǿϴ.");
			$b_hit = 1;
			&K_LOG("$mmonth :  ´ $sangtaeԴϴ.");
		}elsif($mmonth eq "7"){
			&MAP_LOG("<img src=$IMG/j12.gif> <font color=orange>Ȯ</font> ŵξ ϵ�  ?�Ǿϴ.");
			$b_hit = 1;
			&K_LOG("$mmonth :  ´ $sangtaeԴϴ.");
		}
		$eve_date = sprintf("%02d\%02d\", $F_YEAR+$myear, $mmonth);
		$ihit=0;
	($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex) = split(/,/,$ksub1);

		if(!int(rand(20))){
			$ihit=1;
			$ino = int(rand(6));
			if($ino eq 0){
				&MAP_LOG("<img src=$IMG/j8.gif> ?�ѱ�  ƽϴ!");
				&MAP_LOG2("<img src=$IMG/j8.gif> \[$eve_date\]?�ѱ�  ƽϴ!");
			}elsif($ino eq 1){
				&MAP_LOG("<img src=$IMG/j8.gif> ȫ Ͼ�!  ذ ϰ ֽϴ!");
				&MAP_LOG2("<img src=$IMG/j8.gif> \[$eve_date\]ȫ Ͼ�!  ذ ϰ ֽϴ.");
			}elsif($ino eq 2){
				&MAP_LOG("<img src=$IMG/j8.gif>  ϰ ֽϴ. Ÿ  οϰ ֽϴ.");
				&MAP_LOG2("<img src=$IMG/j8.gif> \[$eve_date\] ϰ ֽϴ. Ÿ  οϰ ֽϴ.");
			}elsif($ino eq 3){
				&MAP_LOG("<img src=$IMG/j9.gif> ݳ ǳ   ϴ.");
				&MAP_LOG2("<img src=$IMG/j9.gif> \[$eve_date\]ݳ ǳ   ϴ");
			}elsif($ino eq 4){
				&MAP_LOG("<img src=$IMG/j8.gif>  Ͼ�.");
				&MAP_LOG2("<img src=$IMG/j8.gif> \[$eve_date\] Ͼ�.");
			}elsif($ino eq 5){
				&MAP_LOG("<img src=$IMG/j10.gif>    Ȱ ֽϴ.");
				&MAP_LOG2("<img src=$IMG/j10.gif> \[$eve_date\]   Ȱ ֽϴ.");
			}elsif($ino eq 6){
				&MAP_LOG("<img src=$IMG/j10.gif> ε   � ׽ϴ!");
				&MAP_LOG2("<img src=$IMG/j10.gif> \[$eve_date\]ε   � ׽ϴ!");
			}
		}
		if($b_hit){
		@NEW_TOWN_DATA=();
		foreach(@TOWN_DATA){
			($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$zdef_att,$zsub1,$zsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zname1,$zname2,$zbong1,$zbong2,$zbong3)=split(/<>/);
			if(!int(rand(2.0))){
				$zsouba += int(rand(0.5)*100)/100;
				if($zsouba > 1.2){
					$zsouba = 1.2;
				}
			}else{
				$zsouba -= int(rand(0.5)*100)/100;
				if($zsouba < 0.8){
					$zsouba = 0.8;
				}
			}
			if($zpri >= 50){
	if($zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "â" || $zname eq "Ǿ" || $zname eq ""){
				$znum_add = int(50 * ($zpri - 50));
	}elsif($zname eq "ȫ" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "Ϻ" || $zname eq "" || $zname eq "" || $zname eq ""){
				$znum_add = int(60 * ($zpri - 50));
	}elsif($zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "û" || $zname eq "" || $zname eq "ܾ" || $zname eq "" || $zname eq "ȸ" || $zname eq "" || $zname eq "" || $zname eq ""){
				$znum_add = int(70 * ($zpri - 50));
	}else{
				$znum_add = int(80 * ($zpri - 50));
	}

				if($znum_add < 500){$znum_add=500;}
				$znum += $znum_add;

	if($zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "â" || $zname eq "Ǿ" || $zname eq ""){
	if($znum > 100000){$znum=100000;}
	}elsif($zname eq "ȫ" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "Ϻ" || $zname eq "" || $zname eq "" || $zname eq ""){
	if($znum > 80000){$znum=80000;}
	}elsif($zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "" || $zname eq "û" || $zname eq "" || $zname eq "ܾ" || $zname eq "" || $zname eq "ȸ" || $zname eq "" || $zname eq "" || $zname eq ""){
	if($znum > 65000){$znum=65000;}
	}else{
	if($znum > 50000){$znum=50000;}
	}

			}else{
				$znum -= int(80 * (50 - $zpri));
			}
			if($ihit){
				if($ino eq 0){
					$znou = int($znou * 0.8);
				}elsif($ino eq 1){
					$znou = int($znou * 0.9);
					$zsyo = int($zsyo * 0.9);
					$zshiro = int($zshiro * 0.9);
				}elsif($ino eq 2){
					$znum = int($znum * 0.8);
				}elsif($ino eq 3){
					$znou = int($znou * 1.2);
					if($znou > $znou_max){$znou=$znou_max;}
				}elsif($ino eq 4){
					$znou = int($znou * 0.8);
					$zsyo = int($zsyo * 0.8);
					$zshiro = int($zshiro * 0.8);
					$znum = int($znum * 0.9);
				}elsif($ino eq 5){
					$zsyo = int($zsyo * 1.1);
					if($zsyo > $zsyo_max){$zsyo=$zsyo_max;}
				}elsif($ino eq 6 && zpri < 20){
					$zcon = "";
					$znou = int($znou*0.8);
					$zsyo = int($zsyo*0.8);
					$znum = int($znum*0.8);
					$zsub1 = int($zsub1*0.8);
					$zshiro += 100;
					$zpri = int($zpri*0.8);
					$zdef_att = int($zdef_att*0.8);
				}
			}

			push(@NEW_TOWN_DATA,"$zname<>\$zcon<>\$znum<>\$znou<>\$zsyo<>\$zshiro<>\$znou_max<>\$zsyo_max<>\$zshiro_max<>\$zpri<>\$zx<>\$zy<>\$zsouba<>\$zdef_att<>\$zsub1<>\$zsub2<>\$z[0]<>\$z[1]<>\$z[2]<>\$z[3]<>\$z[4]<>\$z[5]<>\$z[6]<>\$z[7]<>\$zname1<>\$zname2<>\$zbong1<>\$zbong2<>\$zbong3<>\n");
		}
		open(OUT,">$TOWN_LIST");
		print OUT @NEW_TOWN_DATA;
		close(OUT);
		}
		open(OUT,">$month_read");
		print OUT @month_new;
		close(OUT);

	}
	if($ACT_LOG){
		if(@ACT_DATA > 800) { splice(@ACT_DATA,800); }
		open(OUT,">$actfile");
		print OUT @ACT_DATA;
		close(OUT);
	}


	open(IN,"$COUNTRY_LIST") or &ERR2('  ʾҽϴ. err no :country');
	@COU_DATA = <IN>;
	close(IN);
	foreach(@COU_DATA){
		($x2cid,$x2name,$x2ele,$x2mark)=split(/<>/);
		$cou_name[$x2cid] = "$x2name";
		$cou_ele[$x2cid] = "$x2ele";
		$cou_mark[$x2cid] = "$x2mark";
	}


	$country_no=0;$i=1;
	foreach(@COU_DATA){
		($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/);
		if($all_gold){
		$n_gold = int(($xxgold/($all_gold))*1000)/10;
		}else{
		$n_gold = 0;
		}
		if($all_num){
		$n_num  = int(($xxnum/($all_num))*1000)/10;
		}else{
		$n_num  = 0;
		}
		$data_mes .= "<TR><Th bgcolor=$ELE_BG[$xxele] colspan=3><font color=$ELE_C[$xxele]>$xxname</Th></TR><TR><Th bgcolor=$TD_C4>$xxnum($n_num\%)</Th><Th bgcolor=$TD_C4>$xxgold Gold($n_gold\%)</Th><Th bgcolor=$TD_C4>$xxhp/$xxmaxhp</Th></TR>";
		$c_gold[$i] = $xxgold;
		$c_num[$i] = $xxnum; 
		$i++;
	}

	$zmes="";
	$new_date = sprintf("%02d\%02d\", $F_YEAR+$myear, $mmonth);
	$next_time = int(($mtime + $TIME_REMAKE - $date) / 60);

	&HEADER;

	&CHILRANG_INDEX;

	# If admin forced multiple turns, loop TOP again before exiting.
	# STOP_ELIM_TRIGGER (added)
	if ($FORCE_ADMIN_OK && $FORCE_TURN_N > 0 && $FORCE_STOP_ELIM) {
		if (&FORCE_CHECK_ELIM($FORCE_STOP_CID)) {
			$FORCE_TURN_N = 1; # stop after this turn
			if (open(my $LF, ">>./log_file/turn_force.log")) { print $LF time()."<>ADMIN_FORCE_STOP<>CID:$FORCE_STOP_CID<>\n"; close($LF); chmod(0666, "./log_file/turn_force.log"); }
		}
	}

	if ($FORCE_ADMIN_OK && $FORCE_TURN_N > 1) {
		$FORCE_TURN_N--;
		goto TOP_FORCE_REDO;
	}

	exit;

}

	&CHECK_COM;


sub E_LOG2 {
	if($eid ne ""){
		open(IN,"./charalog/log/$eid\.cgi");
		@E_LOG2 = <IN>;
		close(IN);
		unshift(@E_LOG2,"$_[0]($mday$hour$min)\n");
		splice(@E_LOG2,20);

		open(OUT,">./charalog/log/$eid\.cgi");
		print OUT @E_LOG2;
		close(OUT);
	}
}

sub data_save {
        local($datapath) = $_[0];
		local($file) = $_[1];
		local($data) = "$_[2]";
		local($datafile) = $datapath . '/' . $file;
		local($tmpfile) = $datapath . '/' . $file . '.tmp';
		local($tmp_dummy) = $datapath . '/' . $file . "$$\.tmp";
		local($datadir) = $datapath . '/';
		opendir(DIR, $datadir) ;
		@list = readdir(DIR) ;
		closedir(DIR) ;

		if(!open(TMP,">$tmpfile")){
			&ERR2("ӽ  ۼ  ϴ.<br>");
		}elsif(!close(TMP)){			&ERR2("ӽ    ϴ.<br>");
		}elsif(!open(DMY,">$tmp_dummy")){
			&ERR2("ݳ Ͻ ۼ  ϴ.<br>");
		}elsif(!close(DMY)){
			&ERR2("ݳ Ͻ   ϴ.<br>");
		}elsif(!chmod (0777,"$tmp_dummy")){
			&ERR2("ݳ Ͻ Ӽ   ϴ.<br>");
		}elsif(!open(DMY,">$tmp_dummy")){
			&ERR2("ݳ Ͻ   ϴ.<br>");
		}
		print DMY $data;
		if (!close(DMY)){
			&ERR2("ݳ Ͻ   ϴ.<br>");
		}elsif(!rename("$tmp_dummy" , "$datafile")){
			&ERR2("ݳ Ͻ  Ͽ   ϴ.<br>");
		}elsif(!unlink ("$tmpfile")){
			&ERR2("ӽ    ϴ.<br>");
		}
}

sub K_LOG2 {

	open(IN,"./charalog/log/$kid\.cgi");
	@K_LOG2 = <IN>;
	close(IN);
	unshift(@K_LOG2,"$_[0]($mday$hour$min)\n");
	splice(@K_LOG2,20);
	open(OUT,">./charalog/log/$kid\.cgi");
	print OUT @K_LOG2;
	close(OUT);
}


sub SALARY {

	$ksal=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro)=split(/<>/);
		if($z2con eq $kcon){
			if($mmonth eq "1"){
				$ksal += int($z2syo * 8 * $z2num / 16000);
			}elsif($mmonth eq "7"){
				$ksal += int($z2nou * 8 * $z2num / 16000);
			}
		}
	}
}


sub D_F_LOCK {

	local($retry)=1;
	if (-e $lockfile2) {
		local($mtime) = (stat($lockfile2))[9];
		if ($mtime && $mtime < time - 60) { &D_UNLOCK_FILE; }
	}

	while (!mkdir($lockfile2, 0755)) {
		if (--$retry <= 0) { &ERR2("File lock error!<BR> Դϴ.  ٷ ּ.");
}
		sleep(1);
	}
}

sub D_UNLOCK_FILE
{
  rmdir("$lockfile2");
}




sub TOWN_CHANGE{

	local($townpos) = $_[0];

	splice(@TOWN_DATA,$townpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");

}

sub lock #($file_name, $use_lock)
{
	local($file_name, $use_lock) = @_;
	local($lock_flag) = $file_name . ".lock";

	if ($use_lock) {
	local($i) = 0;
#	return -1 if (!-f $file_name);
	rmdir($lock_flag) if (-d $lock_flag && time - (stat($lock_flag))[9] > 60);
	while(!mkdir($lock_flag, 0755)) {	select(undef, undef, undef, 0.05);
		return 0 if (++ $i >= 100);
		}
		return 1;
 	}
 	return 1;
}

sub unlock
{
  rmdir("$_[0].lock") if (-d "$_[0].lock");
}

# -------------------------------------------------------------------------
# [ ڵȭ ]  � Ǵ   ǽð   ( )
# -------------------------------------------------------------------------
sub BOT_PROCESS {
    my ($is_turn_update) = @_;
    my $dir = "./charalog/main";
    my $cmd_dir = "./charalog/command";
    
    unless(-d $cmd_dir) { mkdir($cmd_dir, 0777); }

    # --- AUTO BOT SETUP (added) ---
    if (!-e "./log_file/bot_setup.done") {
        eval { &BOT_AUTO_SETUP(); };
        if (open(my $BS, ">./log_file/bot_setup.done")) { print $BS time(); close($BS); chmod(0666, "./log_file/bot_setup.done"); }
    }


    opendir(DIR, $dir) or return;
    my @files = readdir(DIR);
    closedir(DIR);

    open(IN, "$TOWN_LIST") or return; 
    my @T_LIST = <IN>; 
    close(IN);
    
    open(IN, "./log_file/date_count.cgi"); 
    my $m_line = <IN>;
    close(IN);
    my ($cur_year, $cur_month) = split(/<>/, $m_line);

    # --- BOT DIPLO TURN UPDATE (added) ---
    # Lightweight diplomacy layer used by bots to avoid attacking allies/truce and to create variety.
    if ($is_turn_update) {
        eval { &BOT_DIPLO_TURN_UPDATE($cur_year, $cur_month); };
    }

    my %cmd_map = (
        "" => 1, "" => 2, "" => 29, 
        "�" => 3, "ü" => 30, " Ǭ" => 8, 
        "¡" => 9, "Ʒ" => 11, "Ʒ" => 31, 
        "" => 12, "�" => 13, "̵" => 17, 
        "__MOVE__" => 17,
        "__ATTACK__" => 18,
        "__AGRI__" => 1,
        "__COMM__" => 2,
        "__TECH__" => 29,
        "__RICE__" => 8,
        "__CASTLE__" => 3,
        "__GARRISON__" => 30,
        "__DEF__" => 12,
        "" => 43, "��" => 26
    );

    foreach my $file (@files) {
        next unless ($file =~ /\.cgi$/); 
        my $full_path = "$dir/$file";
        next unless (-f $full_path);

        open(IN, $full_path) or next;
        my @lines = <IN>; 
        close(IN);
        
        my @b = split(/<>/, $lines[0], -1); 
        # �  ǥ ε (16:, 18:, 19:Ʒ, 21:ǥ, 22:, 24:ִ�)
        my ($bid, $bname, $bcon, $bstr, $bint, $blea, $bcha, $bsol, $btra, $bpos, $btarget, $bhost, $bsol_max) = ($b[0], $b[2], $b[10], $b[14], $b[15], $b[16], $b[17], $b[18], $b[19], $b[20], $b[21], $b[22], $b[24]);

        # AI  ĺ (ݸ Ȥ ǥ     �)
        if ($bname =~ /AI_/ || $bhost =~ /bot/i || $bhost eq 'AUTO_BOT' || $bhost eq '' || $bhost eq '' || $btarget ne "") {
            my $date_now = time();
            my $command = ""; my $arg1 = ""; my $arg2 = "";

            if ($bpos eq "" || $bpos >= scalar(@T_LIST)) { next; }
            my @z = split(/<>/, $T_LIST[$bpos]);
            my ($zname, $zcon, $znum, $znou, $zsyo, $zshiro, $znou_max, $zsyo_max, $zshiro_max, $zpri, $ztech, $zx_coord, $zy_coord) = ($z[0], $z[1], $z[2], $z[3], $z[4], $z[5], $z[6], $z[7], $z[8], $z[9], $z[14], $z[10], $z[11]);

            # [  Ǻ]
            my $is_attack_logic = ($bhost eq '' || $btarget ne "" || $bname =~ /\(\)/) ? 1 : 0;

            if ($is_attack_logic) {
                # [] ַ  Ȯ ִ   (  )
                my $safe_max_sol = int($bsol_max);
                if ($safe_max_sol <= 0) { $safe_max_sol = int($blea) * 10 + 500; }
                
                my $cur_sol = int($bsol);
                my $cur_tra = int($btra);

                # 1ܰ: ¡ ( ִġ 1̶   ¡)
                if ($cur_sol < $safe_max_sol) {
                    $command = "¡";
                } 
                # 2ܰ: Ʒ ( áٸ Ʒõ 100 Ʒ)
                elsif ($cur_tra < 100) {
                    $command = "Ʒ";
                } 
                # 3ܰ:  
                else {
                    if ($zcon ne $bcon && $bcon ne "0") {
                        $command = "";
                    } else {
                        #  Ÿ üũ
                        my $is_near = 0;
                        foreach my $t_line (@T_LIST) {
                            my @tz = split(/<>/, $t_line);
                            my ($tname, $tcon, $tx, $ty) = ($tz[0], $tz[1], $tz[10], $tz[11]);
                            if (abs(int($zx_coord) - int($tx)) + abs(int($zy_coord) - int($ty)) == 1) {
                                if (($btarget ne "" && $tname eq $btarget) || ($btarget eq "" && $tcon ne $bcon && $tcon ne "0")) {
                                    $is_near = 1; $arg1 = $tname; last;
                                }
                            }
                        }
                        $command = $is_near ? "�" : "";
                    }
                }
            } 
            # [ ]
            elsif ($zcon eq $bcon && $bcon ne "0") {
                if (int($zpri) < 100) { $command = " Ǭ"; }
                elsif ((int($blea) >= int($bstr) && int($blea) >= int($bint)) && int($zshiro) < int($zshiro_max)) { $command = "ü"; }
                elsif (int($zsyo) < int($zsyo_max)) { $command = ""; }
                elsif (int($znou) < int($znou_max)) { $command = ""; }
                elsif (int($ztech) < 1200) { $command = ""; }
                else { $command = ""; }
            } else {
                $command = "";
            }


            # --- BOT ADVANCED DECISION (added) ---
            # If advanced decision returns a command, override the basic logic.
            my ($bot_cmd, $bot_a1, $bot_a2, $bot_target) = &BOT_DECIDE_ACTION(\@T_LIST, \@z, \@b, $bpos, $bcon, $cur_year, $cur_month);
            if (defined $bot_cmd && $bot_cmd ne '') {
                $command = $bot_cmd;
                $arg1 = $bot_a1;
                $arg2 = $bot_a2;
            }
            if (defined $bot_target && $bot_target ne '') {
                $b[21] = $bot_target; # store target city name
            }

            my $m_id = $cmd_map{$command} || 26;
            my $cmd_file = "$cmd_dir/$bid\.cgi";
            
            # ǽð Ŀǵ   Ʈ (�)
            if (open(CMD, ">$cmd_file")) {
                eval { flock(CMD, 2); };
                for(my $i=0; $i<30; $i++) {
                    print CMD "$m_id<><>$command<>$date_now<>$arg1<>$arg2<><>\n";
                }
                close(CMD);
                chmod(0666, $cmd_file);
            }

            #  Ʈ     ݿ
            if ($is_turn_update) {
                # Token-based internal commands (added)
                if ($command eq "__AGRI__") { $z[3] += 5; }
                elsif ($command eq "__COMM__") { $z[4] += 5; }
                elsif ($command eq "__TECH__") { $z[14] += 3; }
                elsif ($command eq "__CASTLE__") { $z[5] += 5; }
                elsif ($command eq "__GARRISON__") { $z[5] += 2; $z[9] += 1; }
                elsif ($command eq "__DEF__") { $z[5] += 3; }
                elsif ($command eq "__RICE__") { $z[9] += 2; }
                if ($command eq "") { $z[3] += 5; }
                elsif ($command eq "") { $z[4] += 5; }
                elsif ($command eq "ü") { $z[5] += 5; }
                elsif ($command eq "") { $z[14] += 3; }
                elsif ($command eq " Ǭ") { $z[9] += 2; }
                elsif ($command eq "¡") { $b[18] = int($bsol_max || (int($blea) * 10 + 500)); }
                elsif ($command eq "Ʒ") { $b[19] = 100; }
                
                $T_LIST[$bpos] = join('<>', @z) . "\n";
                $b[13] += 2; $b[30] += 5;
                unless($bhost eq '') { $b[22] = 'AUTO_BOT'; }
                
                if (open(OUT, ">$full_path")) { 
                    print OUT join('<>', @b); 
                    close(OUT); 
                }
            }
        }
    }

    if ($is_turn_update) {
        if (open(TOUT, ">$TOWN_LIST")) { 
            eval { flock(TOUT, 2); }; 
            print TOUT @T_LIST; 
            close(TOUT); 
        }
    }
}


# -------------------------------------------------------------------------
# [AUTO BOT SETUP] Create AI players/countries for solo play (non-invasive)
# -------------------------------------------------------------------------
sub BOT_AUTO_SETUP {
    my $dir_main = "./charalog/main";
    my $dir_cmd  = "./charalog/command";
    my $done_flag = "./log_file/bot_setup.done";

    return if (-e $done_flag);

    # If bots already exist, skip.
    if (-d $dir_main) {
        opendir(my $DH, $dir_main);
        my @f = readdir($DH);
        closedir($DH);
        foreach my $ff (@f) {
            if($ff =~ /^bot\d+\.cgi$/i) { return; }
        }
    }

    unless(-d $dir_main) { mkdir($dir_main, 0777); }
    unless(-d $dir_cmd)  { mkdir($dir_cmd, 0777); }

    # Load towns
    open(my $TIN, "$TOWN_LIST") or return;
    my @TOWN = <$TIN>;
    close($TIN);
    return unless @TOWN;

    # Countries: 1..3, simple defaults (ASCII-safe)
    my @COUNTRY_DEF = (
        { cid=>1, name=>'WEI', ele=>1, cap=>0 },
        { cid=>2, name=>'SHU', ele=>2, cap=>1 },
        { cid=>3, name=>'WU',  ele=>3, cap=>2 },
    );

    # --- BOT ADMIN CONFIG OVERRIDE (added) ---
    # Admin can set custom seed countries and capitals via ./log_file/bot_admin.cfg
    my %BOTCFG = &BOT_READ_ADMIN_CFG();

    # Bot editor: force country / scale / stat range (added)
    my $FORCE_CID = int($BOTCFG{'bot_force_country'}||0); # 0=auto
    my $BOT_SCALE = int($BOTCFG{'bot_scale'}||100);       # percent
    if ($BOT_SCALE < 10) { $BOT_SCALE = 10; }
    if ($BOT_SCALE > 500) { $BOT_SCALE = 500; }
    my $STAT_MIN = int($BOTCFG{'bot_stat_min'}||40);
    my $STAT_MAX = int($BOTCFG{'bot_stat_max'}||70);
    if ($STAT_MIN < 1) { $STAT_MIN = 1; }
    if ($STAT_MAX < $STAT_MIN) { $STAT_MAX = $STAT_MIN; }
    if ($STAT_MAX > 200) { $STAT_MAX = 200; }
    if ($BOTCFG{'seed_country_names'} ne '') {
        my @names = split(/\s*,\s*/, $BOTCFG{'seed_country_names'});
        my @caps  = split(/\s*,\s*/, $BOTCFG{'seed_capitals'});
        my @eles  = split(/\s*,\s*/, $BOTCFG{'seed_elements'});
        my @tmp = ();
        for(my $i=0; $i<scalar(@names); $i++) {
            my $nm = $names[$i];
            $nm =~ s/[^A-Za-z0-9_\-\xA1-\xFE]//g; # keep euc-kr bytes too
            if (length($nm) < 4) { $nm = sprintf("BOTNATION%02d", $i+1); }
            my $cap = int($caps[$i] || $i);
            my $el  = int($eles[$i] || ($i%3)+1);
            push(@tmp, { cid=>($i+1), name=>$nm, ele=>$el, cap=>$cap });
        }
        if (scalar(@tmp) > 0) { @COUNTRY_DEF = @tmp; }
    }

    # Seed country lists if empty
    my $country_changed = 0;
    my @COU = ();
    if (open(my $CIN, "$COUNTRY_LIST")) { @COU = <$CIN>; close($CIN); }
    if (!@COU) {
        foreach my $c (@COUNTRY_DEF) {
            push(@COU, $c->{cid}."<>".$c->{name}."<>".$c->{ele}."<>1<>"."bot_leader_".$c->{cid}."<><>"."BOT".$c->{cid}."<>1<><>\n");
        }
        if (open(my $COUT, ">$COUNTRY_LIST")) { print $COUT @COU; close($COUT); chmod(0666, "$COUNTRY_LIST"); }
        $country_changed = 1;
    }

    my @COUN = ();
    if (open(my $CNIN, "$COUNTRY_NO_LIST")) { @COUN = <$CNIN>; close($CNIN); }
    if (!@COUN) {
        foreach my $c (@COUNTRY_DEF) {
            push(@COUN, $c->{cid}."<>".$c->{name}."<>".$c->{ele}."<>1<>"."bot_leader_".$c->{cid}."<><><>1<><>\n");
        }
        if (open(my $CNOUT, ">$COUNTRY_NO_LIST")) { print $CNOUT @COUN; close($CNOUT); chmod(0666, "$COUNTRY_NO_LIST"); }
        $country_changed = 1;
    }

    # Assign capital towns to countries (just first 3 towns for a stable start)
    foreach my $c (@COUNTRY_DEF) {
        my $cap = int($c->{cap});
        next if $cap < 0 || $cap >= scalar(@TOWN);
        my @z = split(/<>/, $TOWN[$cap]);
        $z[1] = $c->{cid};
        $TOWN[$cap] = join('<>', @z);
        $TOWN[$cap] .= "\n" unless $TOWN[$cap] =~ /\n$/;
    }
    if (open(my $TOUT, ">$TOWN_LIST")) { print $TOUT @TOWN; close($TOUT); chmod(0666, "$TOWN_LIST"); }

    # Append bots to member list (optional, for roster)
    my $member_file = "$member_list";
    my @MEM = ();
    if (open(my $MIN, $member_file)) { @MEM = <$MIN>; close($MIN); }
    my $mem_txt = join('', @MEM);

    my $now = time();
    my %CAP_BY_CID = ();
    foreach my $cc (@COUNTRY_DEF) { $CAP_BY_CID{int($cc->{cid})} = int($cc->{cap}); }
    my $bot_index = 1;
    foreach my $c (@COUNTRY_DEF) {
        my @BOT_EACH = split(/\s*,\s*/, ($BOTCFG{'bot_per_country'}||'3,3,3')); my $bot_each = int($BOT_EACH[$c->{cid}-1] || 3);
        for(my $j=0;$j<$bot_each;$j++) {
            my $id = sprintf("bot%03d", $bot_index++);
            my $pass = $id;
            my $name = "AI_General_".$id;
            my $chara = 0;

            # Make stats sum to 200 (editor range aware) (added)
            my $str = $STAT_MIN + int(rand($STAT_MAX - $STAT_MIN + 1));
            my $int = $STAT_MIN + int(rand($STAT_MAX - $STAT_MIN + 1));
            my $lea = $STAT_MIN + int(rand($STAT_MAX - $STAT_MIN + 1));
            my $cha = 200 - ($str+$int+$lea);
            # Keep within range by adjustment
            if ($cha < $STAT_MIN) {
                my $need = $STAT_MIN - $cha;
                my $take = int($need/3) + 1;
                $str -= $take if ($str - $take) >= $STAT_MIN;
                $int -= $take if ($int - $take) >= $STAT_MIN;
                $lea -= $take if ($lea - $take) >= $STAT_MIN;
                $cha = 200 - ($str+$int+$lea);
                if ($cha < $STAT_MIN) { $cha = $STAT_MIN; }
            }
            if ($cha > $STAT_MAX) {
                my $over = $cha - $STAT_MAX;
                $cha = $STAT_MAX;
                # distribute overflow back into other stats
                $str += int($over/3);
                $int += int($over/3);
                $lea += $over - (int($over/3)*2);
            }

            my $sol = 0;
            my $gat = 0;
            my $con = ($FORCE_CID > 0) ? $FORCE_CID : $c->{cid};
            my $gold = int(1000 * $BOT_SCALE / 100);
            my $rice = int(500  * $BOT_SCALE / 100);
            my $cex = 0;
            my $class = 0;
            my $arm = 0;
            my $book = 0;
            my $bank = 16;
            my $sub1 = '';
            my $sub2 = 3590;
            my $pos = ($CAP_BY_CID{int($con)} ne '') ? int($CAP_BY_CID{int($con)}) : int($c->{cap});
            my $mes = '';
            my $host = 'AUTO_BOT';
            my $date = $now;
            my $mail = $id.'@bot.local';
            my $os = 1;
            my $skill = '';
            my $point = 0;
            my $ct = 2;
            my $level = 1;
            my $exp = 0;
            my $codea = '';
            my $codeb = 'A0';
            my $qpoint = 0;

            my $line = join('<>',
                $id,$pass,$name,$chara,$str,$int,$lea,$cha,$sol,$gat,$con,$gold,$rice,$cex,$class,$arm,$book,$bank,$sub1,$sub2,$pos,$mes,$host,$date,$mail,$os,$skill,$point,$ct,$level,$exp,$codea,$codeb,$qpoint,''
            );

            my $path = "$dir_main/$id\.cgi";
            if (open(my $OUT, ">$path")) { print $OUT $line; close($OUT); chmod(0666, $path); }

            # Create initial command file so BOT_PROCESS + existing engine can pick it up
            my $cmd_path = "$dir_cmd/$id\.cgi";
            if (!-f $cmd_path) {
                if (open(my $COUT, ">$cmd_path")) {
                    for(my $k=0;$k<30;$k++){ print $COUT "26<><>\xBC\xF6\xBB\xF6<>$now<><><><><>\n"; }
                    close($COUT);
                    chmod(0666, $cmd_path);
                }
            }

            if ($mem_txt !~ /\Q$name\E<>\Q$id\E<>/ ) {
                push(@MEM, $name."<>".$id."<>\n");
                $mem_txt .= $name."<>".$id."<>\n";
                $country_changed = 1;
            }
        }
    }

    if ($country_changed) {
        if (open(my $MOUT, ">$member_file")) { print $MOUT @MEM; close($MOUT); chmod(0666, $member_file); }
    }
}


# ------------------------------------------------------------------
# BOT_ADVANCED_AI (added)
# - Chooses internal/defense/attack
# - Sets/maintains target city name for strategic focus
# ------------------------------------------------------------------

# Read ./log_file/bot_admin.cfg (simple key<>value per line)
sub BOT_READ_ADMIN_CFG {
    my %cfg = ();
    my $f = "./log_file/bot_admin.cfg";
    if (open(my $IN, $f)) {
        while(my $l = <$IN>) {
            chomp($l);
            next if ($l =~ /^\s*#/ || $l eq "");
            my ($k, $v) = split(/<>/, $l, 2);
            $cfg{$k} = $v;
        }
        close($IN);
    }
    # defaults
    if (!defined $cfg{'bot_total'}) { $cfg{'bot_total'} = 9; }
    if (!defined $cfg{'seed_country_names'}) { $cfg{'seed_country_names'} = ""; }
    if (!defined $cfg{'seed_capitals'}) { $cfg{'seed_capitals'} = "0,1,2"; }
    if (!defined $cfg{'seed_elements'}) { $cfg{'seed_elements'} = "1,2,3"; }
    if (!defined $cfg{'bot_per_country'}) { $cfg{'bot_per_country'} = "3,3,3"; }
    # Personality sliders / diplomacy (added)
    if (!defined $cfg{'bot_aggression'}) { $cfg{'bot_aggression'} = 60; }   # 0..100
    if (!defined $cfg{'bot_internal'})   { $cfg{'bot_internal'}   = 50; }   # 0..100
    if (!defined $cfg{'bot_defense'})    { $cfg{'bot_defense'}    = 50; }   # 0..100
    if (!defined $cfg{'bot_diplomacy'})  { $cfg{'bot_diplomacy'}  = 40; }   # 0..100
    if (!defined $cfg{'bot_diplo_enable'}) { $cfg{'bot_diplo_enable'} = 1; }
    if (!defined $cfg{'bot_strategy'}) { $cfg{'bot_strategy'} = 'BALANCED'; }

    # Bot editor / scale (added)
    if (!defined $cfg{'bot_force_country'}) { $cfg{'bot_force_country'} = 0; } # 0=auto
    if (!defined $cfg{'bot_scale'}) { $cfg{'bot_scale'} = 100; }               # percent
    if (!defined $cfg{'bot_stat_min'}) { $cfg{'bot_stat_min'} = 40; }
    if (!defined $cfg{'bot_stat_max'}) { $cfg{'bot_stat_max'} = 70; }
    return %cfg;
}

# Make a safe bot country name (>=4 chars)
sub BOT_MAKE_COUNTRY_NAME {
    my ($idx) = @_;
    my $n = int($idx || 0);
    my $name = sprintf("BOTNATION%02d", $n);
    # ensure at least 4 chars
    if (length($name) < 4) { $name .= "0000"; }
    return $name;
}



# ------------------------------------------------------------------
# BOT_STRATEGY (added)
# - Strategy presets for target scoring
# ------------------------------------------------------------------
sub BOT_STRATEGY_WEIGHTS {
    my ($p) = @_;
    $p = ($p||'BALANCED');
    my %w = ( tech=>0.12, pri=>1.0, castle=>1400, dist=>25, neutral=>260 );
    if ($p eq 'TECH_FIRST')  { %w = ( tech=>0.25, pri=>0.8, castle=>1200, dist=>22, neutral=>240 ); }
    if ($p eq 'ECON_FIRST')  { %w = ( tech=>0.10, pri=>1.6, castle=>1200, dist=>24, neutral=>240 ); }
    if ($p eq 'CASTLE_WEAK') { %w = ( tech=>0.10, pri=>0.9, castle=>1700, dist=>24, neutral=>260 ); }
    if ($p eq 'DIST_NEAR')   { %w = ( tech=>0.10, pri=>1.0, castle=>1300, dist=>40, neutral=>240 ); }
    return %w;
}

# ------------------------------------------------------------------
# BOT_DIPLO (added)
# - Lightweight diplomacy layer for bots only
# - Stored in ./log_file/bot_diplo.dat
#   A<>B<>STATUS<>UNTIL
#   STATUS: ALLY | TRUCE | WAR
# ------------------------------------------------------------------

sub BOT_DIPLO_KEY {
    my ($a, $b) = @_;
    $a = int($a||0); $b = int($b||0);
    return ($a < $b) ? "$a<>$b" : "$b<>$a";
}

sub BOT_DIPLO_LOAD {
    my %d = ();
    my $f = "./log_file/bot_diplo.dat";
    if (open(my $IN, $f)) {
        while(my $l = <$IN>) {
            chomp($l);
            next if $l eq '';
            my ($a,$b,$st,$until) = split(/<>/, $l, 4);
            my $k = &BOT_DIPLO_KEY($a,$b);
            $d{$k} = { a=>int($a), b=>int($b), st=>($st||'WAR'), until=>int($until||0) };
        }
        close($IN);
    }
    return %d;
}

sub BOT_DIPLO_SAVE {
    my (%d) = @_;
    my $f = "./log_file/bot_diplo.dat";
    unless(-d "./log_file"){ mkdir("./log_file", 0777); }
    if (open(my $OUT, ">$f")) {
        foreach my $k (sort keys %d) {
            my $r = $d{$k};
            next unless ref($r) eq 'HASH';
            print $OUT int($r->{a})."<>".int($r->{b})."<>".($r->{st}||'WAR')."<>".int($r->{until}||0)."\n";
        }
        close($OUT);
        chmod(0666, $f);
    }
}

sub BOT_DIPLO_STATUS {
    my ($a, $b) = @_;
    $a = int($a||0); $b = int($b||0);
    return 'WAR' if ($a <= 0 || $b <= 0 || $a == $b);
    my %d = &BOT_DIPLO_LOAD();
    my $k = &BOT_DIPLO_KEY($a,$b);
    return 'WAR' unless exists $d{$k};
    my $r = $d{$k};
    # Expire truce
    if (($r->{st}||'WAR') eq 'TRUCE' && int($r->{until}||0) > 0 && time() > int($r->{until})) {
        $r->{st} = 'WAR'; $r->{until} = 0;
        $d{$k} = $r;
        &BOT_DIPLO_SAVE(%d);
    }
    return ($r->{st}||'WAR');
}

sub BOT_DIPLO_TURN_UPDATE {
    my ($cur_year, $cur_month) = @_;
    my %cfg = &BOT_READ_ADMIN_CFG();
    return if (int($cfg{'bot_diplo_enable'}||0) != 1);

    # Load countries
    my @COU = ();
    if (open(my $CIN, "$COUNTRY_LIST")) { @COU = <$CIN>; close($CIN); }
    my @cid = ();
    foreach my $l (@COU) {
        my @c = split(/<>/, $l);
        my $id = int($c[0]||0);
        next if $id <= 0;
        push(@cid, $id);
    }
    return if scalar(@cid) < 2;

    my %d = &BOT_DIPLO_LOAD();

    my $dip = int($cfg{'bot_diplomacy'}||40);
    my $agg = int($cfg{'bot_aggression'}||60);
    if ($dip < 0) { $dip = 0; } if ($dip > 100) { $dip = 100; }
    if ($agg < 0) { $agg = 0; } if ($agg > 100) { $agg = 100; }

    # Once per turn, random small number of relationship updates
    my $tries = 1 + int(rand(2));
    for(my $t=0; $t<$tries; $t++) {
        my $a = $cid[int(rand(scalar(@cid)))];
        my $b = $cid[int(rand(scalar(@cid)))];
        next if ($a == $b);
        my $k = &BOT_DIPLO_KEY($a,$b);
        my $cur = $d{$k}->{st} || 'WAR';

        my $r = int(rand(100));
        # Diplomacy high -> ally/truce more likely, Aggression high -> war more likely
        if ($r < int($dip/3)) {
            $d{$k} = { a=>$a, b=>$b, st=>'ALLY', until=>0 };
        }
        elsif ($r < int($dip/3) + int($dip/2)) {
            my $dur = (6*3600) + int(rand(12*3600));
            $d{$k} = { a=>$a, b=>$b, st=>'TRUCE', until=>(time()+$dur) };
        }
        else {
            # War declarations mostly when aggression dominates diplomacy
            my $war_prob = int(($agg - $dip) / 2);
            if ($war_prob < 5) { $war_prob = 5; }
            if (int(rand(100)) < $war_prob) {
                $d{$k} = { a=>$a, b=>$b, st=>'WAR', until=>0 };
            }
        }
    }

    &BOT_DIPLO_SAVE(%d);
}


# ------------------------------------------------------------------
# BOT_EXPEDITION (added)
# - Find strategic target among all towns, then move one step via BFS
# ------------------------------------------------------------------

sub BOT_TOWN_INDEX_BY_NAME {
    my ($T_LIST_REF, $name) = @_;
    my @T_LIST = @{ $T_LIST_REF || [] };
    for(my $i=0; $i<scalar(@T_LIST); $i++) {
        my @tz = split(/<>/, $T_LIST[$i]);
        return $i if (defined $tz[0] && $tz[0] eq $name);
    }
    return -1;
}

sub BOT_BFS_NEXT_STEP {
    my ($T_LIST_REF, $start_idx, $goal_idx) = @_;
    my @T_LIST = @{ $T_LIST_REF || [] };
    return -1 if ($start_idx < 0 || $goal_idx < 0);
    return $start_idx if ($start_idx == $goal_idx);

    # Build coordinate index map
    my %pos2i = ();
    for(my $i=0; $i<scalar(@T_LIST); $i++) {
        my @tz = split(/<>/, $T_LIST[$i]);
        my $x = int($tz[10]||0); my $y = int($tz[11]||0);
        $pos2i{"$x,$y"} = $i;
    }

    my @s = split(/<>/, $T_LIST[$start_idx]);
    my @g = split(/<>/, $T_LIST[$goal_idx]);
    my ($sx,$sy) = (int($s[10]||0), int($s[11]||0));
    my ($gx,$gy) = (int($g[10]||0), int($g[11]||0));

    my @q = (); my %prev = (); my %vis = ();
    my $skey = "$sx,$sy";
    my $gkey = "$gx,$gy";
    push(@q, $skey);
    $vis{$skey} = 1;
    $prev{$skey} = '';

    my @dir = ([1,0],[-1,0],[0,1],[0,-1]);
    while(@q) {
        my $cur = shift(@q);
        last if $cur eq $gkey;
        my ($cx,$cy) = split(/,/, $cur);
        foreach my $d (@dir) {
            my $nx = int($cx) + int($d->[0]);
            my $ny = int($cy) + int($d->[1]);
            my $nk = "$nx,$ny";
            next if $vis{$nk};
            next unless exists $pos2i{$nk};
            $vis{$nk} = 1;
            $prev{$nk} = $cur;
            push(@q, $nk);
        }
    }

    return -1 unless exists $prev{$gkey};
    # Backtrack from goal to find next step after start
    my $cur = $gkey;
    my $p = $prev{$cur};
    while($p ne '' && $p ne $skey) {
        $cur = $p;
        $p = $prev{$cur};
    }
    return -1 if ($p eq '');
    # $cur is one step away from start
    return $pos2i{$cur};
}

sub BOT_DECIDE_ACTION {
    my ($T_LIST_REF, $z_ref, $b_ref, $bpos, $bcon, $cur_year, $cur_month) = @_;
    my @T_LIST = @{ $T_LIST_REF || [] };
    my @z = @{ $z_ref || [] };
    my @b = @{ $b_ref || [] };

    # Character stats (existing slots)
    my $bstr = int($b[14] || 0);  # 무력
    my $bint = int($b[15] || 0);  # 짠�
    my $blea = int($b[16] || 0);  # ����
    my $bcha = int($b[17] || 0);  # 매력
    my $bsol = int($b[18] || 0);
    my $btra = int($b[19] || 0);
    my $btarget = $b[21] || "";

    # Admin-configurable personality sliders
    my %cfg = &BOT_READ_ADMIN_CFG();
    my $AGG  = int($cfg{'bot_aggression'}||60);  # 공격��
    my $INTL = int($cfg{'bot_internal'}||50);    # ������
    my $DEF  = int($cfg{'bot_defense'}||50);     # ��비성
    my $DIP  = int($cfg{'bot_diplomacy'}||40);   # ��교성
    if ($AGG < 0) { $AGG = 0; } if ($AGG > 100) { $AGG = 100; }
    if ($INTL< 0) { $INTL= 0; } if ($INTL> 100) { $INTL= 100; }
    if ($DEF < 0) { $DEF = 0; } if ($DEF > 100) { $DEF = 100; }
    if ($DIP < 0) { $DIP = 0; } if ($DIP > 100) { $DIP = 100; }


# Per-country override (added)
my $CID = int($bcon||0);
if ($CID > 0) {
    if (defined $cfg{"bot_aggression_c$CID"} && $cfg{"bot_aggression_c$CID"} ne '') { $AGG  = int($cfg{"bot_aggression_c$CID"}); }
    if (defined $cfg{"bot_internal_c$CID"}   && $cfg{"bot_internal_c$CID"} ne '')   { $INTL = int($cfg{"bot_internal_c$CID"}); }
    if (defined $cfg{"bot_defense_c$CID"}    && $cfg{"bot_defense_c$CID"} ne '')    { $DEF  = int($cfg{"bot_defense_c$CID"}); }
    if (defined $cfg{"bot_diplomacy_c$CID"}  && $cfg{"bot_diplomacy_c$CID"} ne '')  { $DIP  = int($cfg{"bot_diplomacy_c$CID"}); }
    if ($AGG < 0) { $AGG = 0; } if ($AGG > 100) { $AGG = 100; }
    if ($INTL< 0) { $INTL= 0; } if ($INTL> 100) { $INTL= 100; }
    if ($DEF < 0) { $DEF = 0; } if ($DEF > 100) { $DEF = 100; }
    if ($DIP < 0) { $DIP = 0; } if ($DIP > 100) { $DIP = 100; }
}

# Strategy preset (added)
my $STRAT = $cfg{'bot_strategy'} || 'BALANCED';
if ($CID > 0 && defined $cfg{"bot_strategy_c$CID"} && $cfg{"bot_strategy_c$CID"} ne '') { $STRAT = $cfg{"bot_strategy_c$CID"}; }
my %W = &BOT_STRATEGY_WEIGHTS($STRAT);


    # Town stats
    my $zname = $z[0] || "";
    my $zcon  = $z[1] || "0";
    my $znou  = int($z[3] || 0);
    my $zsyo  = int($z[4] || 0);
    my $zshiro= int($z[5] || 0);
    my $znou_max = int($z[6] || 0);
    my $zsyo_max = int($z[7] || 0);
    my $zshiro_max = int($z[8] || 0);
    my $zpri = int($z[9] || 0);
    my $ztech = int($z[14] || 0);
    my $zx = int($z[10] || 0);
    my $zy = int($z[11] || 0);

    # Heuristic: compute borders and candidate targets
    my @adj_enemy = ();
    my @adj_own   = ();
    foreach my $t_line (@T_LIST) {
        my @tz = split(/<>/, $t_line);
        my ($tname, $tcon, $tx, $ty, $tshiro, $tshiro_max, $tpri, $ttec) = ($tz[0], $tz[1], int($tz[10]||0), int($tz[11]||0), int($tz[5]||0), int($tz[8]||0), int($tz[9]||0), int($tz[14]||0));
        next if ($tname eq "");
        my $d = abs($zx - $tx) + abs($zy - $ty);
        next unless ($d == 1);
        if ($bcon ne "0" && $tcon eq $bcon) { push(@adj_own,   {name=>$tname, con=>$tcon}); }
        elsif ($tcon ne $bcon) {
            # Respect diplomacy for bots (skip allies/truce)
            if ($tcon ne "0") {
                my $st = &BOT_DIPLO_STATUS($bcon, $tcon);
                next if ($st eq 'ALLY' || $st eq 'TRUCE');
            }
            push(@adj_enemy, {name=>$tname, con=>$tcon, shiro=>$tshiro, shiro_max=>$tshiro_max, pri=>$tpri, tec=>$ttec});
        }
    }

    my $is_frontier = (scalar(@adj_enemy) > 0) ? 1 : 0;

    # Determine sol_max safely
    my $bsol_max = int($b[24] || 0);
    if ($bsol_max <= 0) { $bsol_max = int($blea) * 10 + 500; }
    my $sol_ratio = ($bsol_max > 0) ? ($bsol / $bsol_max) : 0;

    # 1) If in neutral/enemy city -> prioritize getting out / stabilize / attack neighbor if possible
    # Keep using existing engine's basic behavior by returning empty here (fall-through) unless we can improve target choice.
    if ($zcon ne $bcon && $bcon ne "0") {
        # If we already have a target and it's adjacent, keep it
        my $keep = 0;
        foreach my $e (@adj_enemy) { if ($btarget ne "" && $e->{name} eq $btarget) { $keep = 1; last; } }
        if (!$keep) {
            # Choose best adjacent target: prefer enemy/neutral (con != ours), lower castle, higher tech/pri
            my $best = "";
            my $best_score = -1e9;
            foreach my $e (@adj_enemy) {
                # Neutral (0) is easier
                my $neutral_bonus = ($e->{con} eq "0") ? 200 : 0;
                my $castle_ratio = ($e->{shiro_max} > 0) ? ($e->{shiro} / $e->{shiro_max}) : 0;
                my $score = $neutral_bonus + (1200 - ($castle_ratio*1200)) + ($e->{tec} / 10) + ($e->{pri});

                my $score2 = $score;
                $score2 = ($W{neutral} + ($W{castle} - ($castle_ratio*$W{castle})) + ($e->{tec}*$W{tech}) + ($e->{pri}*$W{pri}));
                if ($e->{con} eq "0") { $score2 += $W{neutral}; }
                if ($score2 > $best_score) { $best_score = $score2; $best = $e->{name}; }
            }
            if ($best ne "") {
                $b[21] = $best;  # persist target
                return ("", "", "", $best); # don't override base command, only set target
            }
        }
        return ("", "", "", $btarget);
    }

    # 2) If own city: choose among internal/defense/attack
    if ($bcon ne "0" && $zcon eq $bcon) {

        # Personality-adjusted thresholds
        my $def_th = 0.55 + ($DEF * 0.003);          # 0.55..0.85
        my $atk_sol_th = 0.95 - ($AGG * 0.002);      # 0.75..0.95
        my $order_th = 80 + int($INTL * 0.7);        # 80..150
        if ($order_th > 150) { $order_th = 150; }

        # Defense priority if frontier and castle is low
        my $castle_ratio = ($zshiro_max > 0) ? ($zshiro / $zshiro_max) : 1;
        if ($is_frontier && $castle_ratio < $def_th) {
            # Prefer explicit castle/defense commands (added)
            # - __CASTLE__: ���/�� 강화
            return ("__CASTLE__", "", "", $btarget);
        }

        # Attack priority if frontier and ready
        if ($is_frontier && $sol_ratio >= $atk_sol_th && $btra >= 100) {
            # choose/refresh target among adjacent enemies
            my $best = "";
            my $best_score = -1e9;
            foreach my $e (@adj_enemy) {
                my $neutral_bonus = ($e->{con} eq "0") ? 250 : 0;
                my $castle_ratio2 = ($e->{shiro_max} > 0) ? ($e->{shiro} / $e->{shiro_max}) : 0;
                my $score = $neutral_bonus + (1400 - ($castle_ratio2*1400)) + ($e->{tec}/8) + ($e->{pri});

                my $score2 = $score;
                $score2 = ($W{neutral} + ($W{castle} - ($castle_ratio2*$W{castle})) + ($e->{tec}*$W{tech}) + ($e->{pri}*$W{pri}));
                if ($e->{con} eq "0") { $score2 += $W{neutral}; }
                if ($score2 > $best_score) { $best_score = $score2; $best = $e->{name}; }
            }
            if ($best ne "") {
                $b[21] = $best;
                # Attack command uses arg1 as target city name in original logic ("�")
                return ("�", $best, "", $best);
            }
        }

        # Expedition: if no adjacent targets, move toward a strategic target
        if (!$is_frontier && $AGG >= 55 && $sol_ratio >= 0.70 && $btra >= 50) {
            my $goal_name = $btarget;
            my $goal_idx = -1;
            if ($goal_name ne '') {
                $goal_idx = &BOT_TOWN_INDEX_BY_NAME(\@T_LIST, $goal_name);
            }
            # If no saved target or invalid, pick a new global target
            if ($goal_idx < 0) {
                my $best = "";
                my $best_score = -1e9;
                for(my $i=0; $i<scalar(@T_LIST); $i++) {
                    my @tz = split(/<>/, $T_LIST[$i]);
                    my ($tname,$tcon,$tx,$ty,$tshiro,$tshiro_max,$tpri,$ttec) = ($tz[0], $tz[1], int($tz[10]||0), int($tz[11]||0), int($tz[5]||0), int($tz[8]||0), int($tz[9]||0), int($tz[14]||0));
                    next if ($tname eq '' || $tcon eq $bcon);
                    # Respect diplomacy
                    if ($tcon ne "0") {
                        my $st = &BOT_DIPLO_STATUS($bcon, $tcon);
                        next if ($st eq 'ALLY' || $st eq 'TRUCE');
                    }
                    my $neutral_bonus = ($tcon eq "0") ? 260 : 0;
                    my $castle_ratio2 = ($tshiro_max > 0) ? (int($tshiro)/int($tshiro_max)) : 0;
                    my $dist = abs($zx - $tx) + abs($zy - $ty);
                    my $score = $neutral_bonus + (1500 - ($castle_ratio2*1500)) + ($ttec/6) + ($tpri) - ($dist*25);

                    my $score2 = $score;
                    $score2 = ($W{neutral} + ($W{castle} - ($castle_ratio2*$W{castle})) + ($ttec*$W{tech}) + ($tpri*$W{pri}) - ($dist*$W{dist}));
                    if ($tcon eq "0") { $score2 += $W{neutral}; }
                    if ($score2 > $best_score) { $best_score = $score2; $best = $tname; $goal_idx = $i; }
                }
                if ($best ne '') { $goal_name = $best; $b[21] = $best; }
            }

            if ($goal_idx >= 0 && $goal_name ne '' && $goal_name ne $zname) {
                my $next_idx = &BOT_BFS_NEXT_STEP(\@T_LIST, int($bpos), int($goal_idx));
                if ($next_idx >= 0 && $next_idx != int($bpos)) {
                    return ("__MOVE__", "", $next_idx, $goal_name);
                }
            }
        }

        # Internal affairs: order first, then agriculture/commerce/tech (added)
        # - __RICE__: �/치안
        # - __AGRI__: ����
        # - __COMM__: ����
        # - __TECH__: 기술
        if ($zpri < $order_th) { return ("__RICE__", "", "", $btarget); }

        # Decide best internal action by gaps + ability
        my $gap_nou = $znou_max - $znou; if ($gap_nou < 0) { $gap_nou = 0; }
        my $gap_syo = $zsyo_max - $zsyo; if ($gap_syo < 0) { $gap_syo = 0; }
        my $gap_tec = 1200 - $ztech; if ($gap_tec < 0) { $gap_tec = 0; }

        # Score each choice
        my $sc_agri = ($gap_nou * 3) + ($bint * 2) + ($INTL);
        my $sc_comm = ($gap_syo * 3) + ($bcha * 2) + ($INTL);
        my $sc_tech = ($gap_tec * 2) + ($bint * 3) + int($W{tech} || 1);

        # Frontier: if defensive leaning, also consider garrison / defense facility even when castle is ok
        if ($is_frontier && $DEF >= 65) {
            # __GARRISON__: ��비� / 병력 ���
            # __DEF__: 방어����
            if ($sol_ratio < 0.85) { return ("__GARRISON__", "", "", $btarget); }
            if ($castle_ratio < 0.92) { return ("__DEF__", "", "", $btarget); }
        }

        # Choose highest score
        if ($sc_tech >= $sc_agri && $sc_tech >= $sc_comm && $gap_tec > 0 && $bint >= 60) { return ("__TECH__", "", "", $btarget); }
        if ($sc_agri >= $sc_comm && $gap_nou > 0) { return ("__AGRI__", "", "", $btarget); }
        if ($gap_syo > 0) { return ("__COMM__", "", "", $btarget); }

        return ("", "", "", $btarget);
    }

    return ("", "", "", $btarget);
}

sub ERR2 { print "Content-type: text/html\n\n$_[0]"; exit; }
sub DECODE { 
    if ($ENV{'REQUEST_METHOD'} eq "POST") { read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'}); }
    else { $buffer = $ENV{'QUERY_STRING'}; }
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs) {
        ($name, $value) = split(/=/, $pair);
        $value =~ tr/+/ /;
        $value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
        &jcode::convert(\$value, 'euc', 'sjis');
        $FORM{$name} = $value;
    }
}
1;