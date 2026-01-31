#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require './dataroot/index1.cgi'; #    Œµ ƒ° 
require './dataroot/index2.cgi';
require 'suport.cgi';

if($MENTE) { &ERR2("Œµ‘¥œ¥. √∏ Ÿ∑ ÷Ω Ω√ø"); }
&DECODE;
$adminid = "pwh857";
$adminpass = "921002";

$adminid2 = "⁄æÃµ2";
$adminpass2 = "⁄æÃµ2";

$adminid3 = "⁄æÃµ3";
$adminpass3 = "⁄æÃµ3";

# -----------------------------------------------------
#  –± √≥
# -----------------------------------------------------
if($mode eq 'CHANGE') { &CHANGE; }
elsif($mode eq 'CHANGE2') { &CHANGE2; }
elsif($mode eq 'MENTE') { &MENTE; }
elsif($mode eq 'MENTE1') { &MENTE1; }
elsif($mode eq 'MENTE2') { &MENTE2; }
elsif($mode eq 'QUEST_ENTRY') { &QUEST_ENTRY; }
elsif($mode eq 'QUEST_EDIT') { &QUEST_EDIT; }
elsif($mode eq 'QUEST_EDIT_COM') { &QUEST_EDIT_COM; }
elsif($mode eq 'QUEST_ADD') { &QUEST_ADD; }
elsif($mode eq 'QUEST_ADD_COM') { &QUEST_ADD_COM; }
elsif($mode eq 'BBS') { &BBS; }
elsif($mode eq 'GG') { &GG; }
elsif($mode eq 'GG1') { &GG1; }
elsif($mode eq 'CHANGE1') { &CHANGE1; }
elsif($mode eq 'DEL') { &DEL; }
elsif($mode eq 'DEL2') { &DEL2; }
elsif($mode eq 'DEL_LIST') { &DEL_LIST; }
elsif($mode eq 'ALL_DEL') { &ALL_DEL; }
elsif($mode eq 'INIT_DATA') { &INIT_DATA; }
elsif($mode eq 'EVENT_ON') { &EVENT_ON; }
elsif($mode eq 'MAKE_BOT') { &MAKE_BOT; } 
elsif($mode eq 'BOT_ADMIN') { &BOT_ADMIN; }
elsif($mode eq 'BOT_ADMIN_SAVE') { &BOT_ADMIN_SAVE; }

elsif($mode eq 'BOT_DIPLO_SET') { &BOT_DIPLO_SET; }
else{&TOP;}

sub TOP {

if(($in{'id'} eq "$adminid" && $in{'pass'} eq "$adminpass")){
	&HEADER;
	print <<"EOM";
<h2></h2>
<CENTER>
<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><TBODY bgcolor=$TD_C4>
<TR><TH colspan=2>ﬁ¥</TH></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=MENTE>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='ƒ≥ '>
</Th></form><TD>
√∑Ãæ Õ∏ ’¥œ¥. “ø  ø ÷º.
</TD></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=INIT_DATA>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value=' ±»≠'>
</Th></form><TD>
 Õ∏  ±»≠’¥œ¥.
</TD></TD></TR>

<!--   ﬁ¥ -->
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=MAKE_BOT>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='⁄µ»≠  '>
</Th>
<TD>
 ≈≠ AI () ’¥œ¥.<br>
 : <input type=text name=bot_count size=5 value=1>  | 
»£: <input type=text name=con_no size=5 value=0> (0:“º)
</TD></TR>
</form>
<!-- //  ﬁ¥ -->

<!-- BOT ADMIN (added) -->
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=BOT_ADMIN>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='BOT ﬁ¥'>
</Th>
<TD>
 Î¥/ÍµÍ∞ ù¥Î¶/Î∞∞Ïπò(àòèÑ) Ñ§†ï
</TD></TR>
</form>
<!-- // BOT ADMIN (added) -->


<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=QUEST_ENTRY>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='∆Æ€º'>
</Th></form><TD>
∆Æ €º’¥œ¥.
</TD></TD></TR>

</TBODY></TABLE>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=EVENT_ON>
<input type=hidden name=mode1 value=1>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='Ã∫∆Æ'></form>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=EVENT_ON>
<input type=hidden name=mode1 value=2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='Ã∫∆Æ»∏'></form>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=EVENT_ON>
<input type=hidden name=mode1 value=3>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='Ã∫∆Æ'></form>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BBS>
:<input type=text name=message size=40>
URL≈©:<input type=text name=message1 size=40>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='€æ'>
<br></form>

<form method="post" action="dkajlfjeioaefhoiwqhfeouihwefwefksdjklfjwe.cgi">
</select><input type=submit value=' '>
<br></form>
</CENTER>

EOM
}elsif(("$adminid3" eq $in{'id'} && $in{'pass'} eq "$adminpass3")){
    # ... (ŒøÓø ⁄µ ) ...
    &HEADER;
    print <<"EOM";
<h2></h2>
<CENTER>
<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><TBODY bgcolor=$TD_C4>
<TR><TH colspan=2>ŒøÓø ﬁ¥</TH></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=MENTE1>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='ƒ≥ '>
</Th></form><TD>
√∑Ãæ Õ∏ ’¥œ¥.
</TD>
<!-- ... -->
</TBODY></TABLE>
EOM
}elsif(("$adminid2" eq $in{'id'} && $in{'pass'} eq "$adminpass2")){
    # ... (∆Æƒø ⁄µ ) ...
    &HEADER;
    print <<"EOM";
<h2></h2>
<CENTER>
<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><TBODY bgcolor=$TD_C4>
<TR><TH colspan=2>∆Æƒø ﬁ¥</TH></TR>
<form method="post" action="admin.cgi">
<TR><Th>
<input type=hidden name=mode value=QUEST_ENTRY>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='∆Æ€º'>
</Th></form><TD>
∆Æ €º’¥œ¥.
</TD></TD></TR>
</TBODY></TABLE>
EOM
}else{&ERR2("ID, –Ω  $num ");}
	open(IN,"$ADMIN_BBS");
	@A_BBS = <IN>;
	close(IN);

print "<center><table width=80% border=0 >@A_BBS</table></center>";

	&FOOTER;
	exit;
}

# -------------------------------------------------------------------------
# MAKE_BOT ∆æ :  ⁄µ  (ƒ°  »≠)
# -------------------------------------------------------------------------
sub MAKE_BOT {
    if ($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass") { &ERR2(" œ¥."); }
    if ($in{'bot_count'} !~ /^[0-9]+$/) { &ERR2(" Œø ⁄∏ ‘∑œº."); }
    if ($in{'con_no'} eq "") { $in{'con_no'} = 0; }

    my $count = $in{'bot_count'};
    my $country = $in{'con_no'};
    my $cur_time = time();
    my $created_cnt = 0;
    
    # [ƒ°  ]
    my $target_pos = 0; 
    my $king_name_found = "";
    my $debug_msg = "";

    if ($country > 0) {
        # 1.   √£ (  √µ)
        my $c_file = "";
        if ($COUNTRY_LIST && -e $COUNTRY_LIST) {
            $c_file = $COUNTRY_LIST;
        } elsif (-e "./data/country.cgi") {
            $c_file = "./data/country.cgi";
        } elsif (-e "./dataroot/country.cgi") {
            $c_file = "./dataroot/country.cgi";
        }

        if ($c_file && open(IN, "$c_file")) {
            my @cou_lines = <IN>;
            close(IN);
            
            my $king_id = "";
            $debug_msg .= "($c_file) . ";
            
            foreach my $line (@cou_lines) {
                my ($xcid, $xname, $xele, $xmark, $xking) = split(/<>/, $line);
                if ($xcid == $country) {
                    $king_id = $xking;
                    $debug_msg .= "($xcid) ID($xking) √£. ";
                    last;
                }
            }
            
            if ($king_id) {
                # 2.   –±
                if (open(K, "./charalog/main/$king_id.cgi")) {
                    my $k_line = <K>;
                    close(K);
                    my @k_data = split(/<>/, $k_line);
                    $target_pos = $k_data[20]; # 21¬∞: pos
                    $king_name_found = $k_data[2];
                    $debug_msg .= "($king_name_found) ƒ°($target_pos) »Æ.";
                } else {
                    $debug_msg .= "($king_id.cgi) √£.";
                }
            } else {
                $debug_msg .= "ÿ¥  »£  .";
            }
        } else {
            $debug_msg .= "   √£($COUNTRY_LIST).";
        }
    } else {
        $debug_msg = "“º(0 ) .";
    }

    # 3.  
    for (my $i = 1; $i <= $count; $i++) {
        my $bot_num = int(rand(9999));
        my $bot_id = "bot_" . $cur_time . "_" . $i; 
        my $bot_pass = "botpass";
        my $bot_name = "AI_" . $bot_num;

        my $str = int(rand(31)) + 50; 
        my $int = int(rand(31)) + 50; 
        my $lea = int(rand(31)) + 50; 
        my $cha = int(rand(31)) + 50; 

        # ƒ°($target_pos) 
        my $bot_data = "$bot_id<>$bot_pass<>$bot_name<>0<>$str<>$int<>$lea<>$cha<>0<>100<>$country<>3000<>3000<>0<>0<>0<>0<>0<>0<>0<>$target_pos<>œπ›∏<>AUTO_BOT<>$cur_time<>bot\@system<>1<>0<>0<>0<>1<>0<>\n";
        
        open(OUT, ">./charalog/main/$bot_id.cgi");
        print OUT $bot_data;
        close(OUT);
        $created_cnt++;
    }

    &HEADER;
    print <<"EOM";
    <center>
    <h2>$created_cnt  (AI)  œ∑.</h2>
    <hr size=0>
    <br>
    <b>[ ∆Æ]</b><br>
    -  : $country <br>
    - ƒ° ƒ°: $target_pos  <br>
    -  ± ⁄ø:  3000,  3000,  0<br>
    - ÷∏: $king_name_found<br>
    -  : <font color=blue>$debug_msg</font><br>
    <br>
    <form method="post" action="admin.cgi">
    <input type=hidden name=id value="$in{id}">
    <input type=hidden name=pass value="$in{pass}">
    <input type=submit value='∆∞'>
    </form>
    </center>
EOM
    &FOOTER;
    exit;
}

sub EVENT_ON{

	
	open(IN,"./log_file/event_on.cgi");
	@EVENT = <IN>;
	close(IN);

	($eventon,$emoney,$etime) = split(/<>/,$EVENT[0]);

	if($in{'mode1'} == 1){
	$eventon = 1;
	$emoney = 0;
	$etime = time();
	}elsif($in{'mode1'} ==2){
	$eventon = 2;
	}else{
	$eventon = 0;
	$emoney = 0;
	}



	@EVENT_DATA=();
	unshift(@EVENT_DATA,"$eventon<>$emoney<>$etime<>");
	open(OUT,">./log_file/event_on.cgi") or &ERR('MAIN Œø Õ∏   œ¥.');
	print OUT @EVENT_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>÷¥»∏Ã∫∆Æ «æœ¥.</h2><p>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='∆ø¬¥'>
</form></CENTER>
EOM

	&FOOTER;

	exit;

}



sub MENTE {

$dir="./charalog/main";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "Àª : $dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file ﬂ∞ﬂµ  æ“Ωœ¥.<br>\n";
			return 1;
		}
		@page = <page>;
		close(page);
		$list[$i]="$file";
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$page[0]);

		if("$in{'serch'}" ne ""){
			if("$ename" =~ "$in{'serch'}"){
				$human_data[$i]="$ehost<>$ename<>$eid<>";
			}else{
				next;
			}
		}else{
			if($in{'no'} eq "2"){
				$human_data[$i]="$ename<>$ehost<>$eid<>$epass<>$email<>$eos<>";
			}elsif($in{'no'} eq "3"){
				$human_data[$i]="$eid<>$ehost<>$ename<>$epass<>$email<>$eos<>";
			}elsif($in{'no'} eq "4"){
				$human_data[$i]="$epass<>$ehost<>$ename<>$eid<>$email<>$eos<>";
			}elsif($in{'no'} eq "5"){
				$human_data[$i]="$email<>$epass<>$ehost<>$ename<>$eid<>$eos<>";
			}elsif($in{'no'} eq "6"){
				$human_data[$i]="$eos<>$ename<>$ehost<>$eid<>$epass<>$email<>";
			}else{
				$human_data[$i]="$ehost<>$ename<>$eid<>$epass<>$email<>$eos<>";
			}
		}
		push(@newlist,"@page<br>");
		$i++;
	}
}
	closedir(dirlist);

	@human_data = sort @human_data;

$tt = time - (60 * 60 * 24 * 34);
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($tt);
$year += 1900;
$mon++;
$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);


	&HEADER;
	print <<"EOM";
<h2>ƒ≥ </h2>
<br>
ID œ∏  «æ  ÷º.<br>
»£∆Æ √∑ œ∞ ÷Ωœ¥.<br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CHANGE>œ¥  : 
<select name=fileno>
EOM
$i=0;$w_host="";
foreach(@human_data){
	if($in{'no'} eq "2"){
		($ename,$ehost,$eid,$epass,$email,$eos) = split(/<>/);
	}elsif($in{'no'} eq "3"){
		($eid,$ehost,$ename,$epass,$email,$eos) = split(/<>/);
	}elsif($in{'no'} eq "4"){
		($epass,$ehost,$ename,$eid,$email,$eos) = split(/<>/);
	}elsif($in{'no'} eq "5"){
		($email,$epass,$ehost,$ename,$eid,$eos) = split(/<>/);
	}elsif($in{'no'} eq "6"){
		($eos,$ename,$ehost,$eid,$epass,$email) = split(/<>/);
	}else{
		($ehost,$ename,$eid,$epass,$email,$eos) = split(/<>/);
	}
	print "<option value=$eid\.cgi>:$eos›£ID:$eid›£Ã∏:$ename›£»£∆Æ:$ehost›£€∫:$epass›£Ã∏:$email\n";
	if($in{'no'} eq "" || $in{'no'} eq "1"){
		if($w_host eq "$ehost"){
			$mess .= "$ename | $w_name<BR>\n";
		}
	}
	$w_host = "$ehost";
	$w_name = "$ename";
	$i++;
}
print <<"EOM";
</select><input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value=''>
<br></form>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=MENTE>
<br><input type=radio name=no value="1">»£∆Æ (<font color=red>2  √º≈©</font>)<br>
<input type=radio name=no value="2">Ã∏<br>
<input type=radio name=no value="3">ID<br>
<input type=radio name=no value="4"><br>
<input type=radio name=no value="5">Ã∏<br>
<input type=radio name=no value="6"> (Yes:1 | No:0)<br>
Ã∏Àª<input type=text name=serch size=20><br>
<input type=submit value=''>
<br></form>

<h2> </h2>
2ﬂµ⁄∏  ’¥œ¥.<BR>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=DEL_LIST>
<input type=submit value=' ∆Æ'>
<br></form>


2ﬂµ «Ω(Ã∞ ﬂ¥   ‘¥œ¥. by ƒ•)<p>
<font color=red>$mess</font>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='TOP'>
<br></form>

EOM
	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
print "@A_LOG";
	&FOOTER;
	exit;
}

sub MENTE1 {


$dir="./charalog/main";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "Àª : $dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file ﬂ∞ﬂµ  æ“Ωœ¥.<br>\n";
			return 1;
		}
		@page = <page>;
		close(page);
		$list[$i]="$file";
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$page[0]);

		if("$in{'serch'}" ne ""){
			if("$ename" =~ "$in{'serch'}"){
				$human_data[$i]="$ehost<>$ename<>$eid<>";
			}else{
				next;
			}
		}else{
			if($in{'no'} eq "2"){
				$human_data[$i]="$ename<>$ehost<>$eid<>$email<>$eos<>";
			}elsif($in{'no'} eq "3"){
				$human_data[$i]="$eid<>$ehost<>$ename<>$email<>$eos<>";
			}elsif($in{'no'} eq "5"){
				$human_data[$i]="$email<>$ehost<>$ename<>$eid<>";
			}elsif($in{'no'} eq "6"){
				$human_data[$i]="$eos<>$ename<>$ehost<>$eid<>$email<>";
			}else{
				$human_data[$i]="$ehost<>$ename<>$eid<>$email<>$eos<>";
			}
		}
		push(@newlist,"@page<br>");
		$i++;
	}
}
	closedir(dirlist);

	@human_data = sort @human_data;

$tt = time - (60 * 60 * 24 * 34);
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($tt);
$year += 1900;
$mon++;
$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);


	&HEADER;
	print <<"EOM";
<h2>ƒ≥ </h2>
<br>
ID œ∏  «æ  ÷º.<br>
»£∆Æ √∑ œ∞ ÷Ωœ¥.<br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CHANGE1>œ¥  : 
<select name=fileno>
EOM
$i=0;$w_host="";
foreach(@human_data){
	if($in{'no'} eq "2"){
		($ename,$ehost,$eid,$email,$eos) = split(/<>/);
	}elsif($in{'no'} eq "3"){
		($eid,$ehost,$ename,$email,$eos) = split(/<>/);
	}elsif($in{'no'} eq "5"){
		($email,$ehost,$ename,$eid,$eos) = split(/<>/);
	}elsif($in{'no'} eq "6"){
		($eos,$ename,$ehost,$eid,$email) = split(/<>/);
	}else{
		($ehost,$ename,$eid,$email,$eos) = split(/<>/);
	}
	print "<option value=$eid\.cgi>:$eos›£ID:$eid›£Ã∏:$ename›£»£∆Æ:$ehost›£Ã∏:$email\n";
	if($in{'no'} eq "" || $in{'no'} eq "1"){
		if($w_host eq "$ehost"){
			$mess .= "$ename | $w_name<BR>\n";
		}
	}
	$w_host = "$ehost";
	$w_name = "$ename";
	$i++;
}
print <<"EOM";
</select><input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value=''></form>
<br>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=MENTE1>
<br><input type=radio name=no value="1">»£∆Æ (<font color=red>2  √º≈©</font>)<br>
<input type=radio name=no value="2">Ã∏<br>
<input type=radio name=no value="3">ID<br>
<input type=radio name=no value="5">Ã∏<br>
<input type=radio name=no value="6">(Yes:1 | No:0)<br>
Ã∏Àª<input type=text name=serch size=20><br>
<input type=submit value=''>
<br></form>

<h2> </h2>
2ﬂµ⁄∏  ’¥œ¥.<BR>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=DEL_LIST>
<input type=submit value=' ∆Æ'>
<br></form>


2ﬂµ «Ω(Ã∞ ﬂ¥ ƒ≥Õµ  ‹πŸ∂œ¥. by ƒ•)<p>
<font color=red>$mess</font>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='TOP'>
<br></form>

EOM
	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
print "@A_LOG";
	&FOOTER;
	exit;
}


sub BBS {

	&TIME_DATA;

	if($in{'id'} eq "$adminid"){
	$goodname = "[Gm]";
	$goodname1 = "b20";
	}elsif($in{'id'} eq "$adminid1"){
	$goodname = "[Gm]";
	$goodname1 = "gm1";
	}elsif($in{'id'} eq "$adminid2"){
	$goodname = "[Gm]";
	$goodname1 = "gm2";
	}elsif($in{'id'} eq "$adminid3"){
	$goodname = "[Gm]";
	$goodname1 = "gm3";
	}

	open(IN,"$ADMIN_BBS");
	@AD_DATA = <IN>;
	close(IN);

	if($in{'message'} eq "") { &ERR2("ﬁº ‘µ«æ   Ωœ¥."); }
	if(length($in{'message'}) > 50) { &ERR2("  œ∞  ÷º"); }

	$bbs_num = @AD_DATA;
	if($bbs_num > 40) { pop(@AD_DATA); }

	&MAP_LOG3("[$goodname] <a href=$in{'message1'} target=_blank>$in{'message'}</a>");

	unshift(@AD_DATA,"<font color=red>$in{'message'}</font> $goodname ($mday$hour$min)<BR><hr size=0>\n");

	open(OUT,">$ADMIN_BBS");
	print OUT @AD_DATA;
	close(OUT);

	&HEADER;
	print <<"EOM";
<h2>ﬂΩœ¥.</h2>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='∆ø¬¥'>
<br></form>
EOM
	&FOOTER;
	exit;
}

sub CHANGE {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("ID, –Ω  $num ");}
	$dir="./charalog/main";
	if(!open(page,"$dir/$in{'fileno'}")){
		$datames .= "$dir/$file ﬂ∞ﬂµ  æ“Ωœ¥.<br>\n";
		return 1;
	}
	@page = <page>;
	close(page);
	
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$page[0]);
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($edate);
	$year += 1900;
	$mon++;
	$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
	$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);
	
	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<h3><img src="$IMG/$echara.gif" width="$img_wid" height="$img_height" border=0> <font size=5 color=orange>$ename</font> </h3>
<table>
<tr>
<th>ID</th><td><input type=text name=eid value='$eid'></td>
<th>PASS</th><td><input type=text name=epass value='$epass'></td>
<th>NAME</th><td><input type=text name=ename value='$ename'></td>
<th>◊∏ ID</th><td><input type=text name=echara value='$echara'></td>
<tr>
<th></th><td><input type=text name=estr value='$estr'></td>
<th></th><td><input type=text name=eint value='$eint'></td>
<th>÷∑</th><td><input type=text name=elea value='$elea'></td>
<th>≈∑</th><td><input type=text name=echa value='$echa'></td>
</TR>
<tr>
<th></th><td><input type=text name=esol value='$esol'></td>
<th>∆∑</th><td><input type=text name=egat value='$egat'></td>
<th></th><td><input type=text name=econ value='$econ'></td>
<th></th><td><input type=text name=egold value='$egold'></td>
</TR>
<tr>
<th></th><td><input type=text name=erice value='$erice'></td>
<th></th><td><input type=text name=ecex value='$ecex'></td>
<th>ƒ°</th><td><input type=text name=eclass value='$eclass'></td>
<th></th><td><input type=text name=earm value='$earm'></td>
</TR>
<tr>
<th></th><td><input type=text name=ebook value='$ebook'></td>
<th>Êº</th><td><input type=text name=ebank value='$ebank'></td>
<th>1</th><td><input type=text name=esub1 value='$esub1'></td>
<th>2</th><td><input type=text name=esub2 value='$esub2'></td>
</TR>
<tr>
<th> ƒ°</th><td><input type=text name=epos value='$epos'></td>
<th>ﬁΩ</th><td><input type=text name=emes value='$emes'></td>
<th>»£∆Æ</th><td><input type=text name=ehost value='$ehost'></td>
<th>œΩ</th><td><input type=text name=edate value='$edate'></td>
</TR>
<tr>
<th>MAIL</th><td><input type=text name=email value='$email'></td>
<th>‡µ √º≈©</th><td><input type=text name=eos value='$eos'></td>
<th>∆Ø</th><td><input type=text name=eskill value='$eskill'></td>
<th>∆Ø∆Æ</th><td><input type=text name=epoint value='$epoint'></td>
</TR>
<tr>
<th></th><td><input type=text name=ect value='$ect'></td>
<th></th><td><input type=text name=elevel value='$elevel'></td>
<th>ƒ°</th><td><input type=text name=eexp value='$eexp'></td>
<th>∆Æ</th><td><input type=text name=ecodea value='$ecodea'></td>
</TR>
<tr>
<th>∆Æ</th><td><input type=text name=ecodeb value='$ecodeb'></td>
<th>∆Æ∆Æ</th><td><input type=text name=eqpoint value='$eqpoint'></td>
<th></th><td></td>
<th></th><td></td>
</TR>



</table>
<br>
<input type=hidden name=mode value=CHANGE2>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value=''>
<br></form><form method="post" action="admin.cgi">
<input type=hidden name=mode value=GG>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='»Æ'>
<br></form><form method="post" action="admin.cgi">
<input type=hidden name=mode value=GG1>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value=''>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value=' ◊∏–¥'>
</form>
<br>
<br>
<br>
<br>
MAP Œ± <br>
<form method="post" action="admin.cgi">
<input type=hidden name=filename value=$in{'fileno'}>
<input type=hidden name=mode value=DEL>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='  '>
</form>
<br>
<br>
<br>
MAP Œ± <br>
<form method="post" action="admin.cgi">
<input type=hidden name=filename value=$in{'fileno'}>
<input type=hidden name=mode value=DEL2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='  '>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

sub DEL {

&HOST_NAME;
	open(IN,"./charalog/main/$in{'filename'}") or &ERR2('    œ¥.');
	@CN_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);
			&BONG_DEL;
			$dir2="./charalog/main";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/log";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/command";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/log2";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/history";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/per";
			unlink("$dir2/$in{'filename'}");

&ADMIN_LOG("<font color=red>$kname ﬂΩœ¥. $host </font>");

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	&TIME_DATA;
	open(IN,"$DEF_LIST");
	@DEF_LIST = <IN>;
	close(IN);

	@NEW_DEF_LIST_DEL=();
	foreach(@DEF_LIST){
		($tid,$tname,$ttown_id,$ttown_flg,$tcon) = split(/<>/);
		if("$tid" eq "$kid"){
		}else{
			push(@NEW_DEF_LIST_DEL,"$_");
		}
	}
	open(OUT,">$DEF_LIST");
	print OUT @NEW_DEF_LIST_DEL;
	close(OUT);

	unshift(@S_MOVE,"<img src=$IMG/j17.gif> $kname «æœ¥.($mday$hour$min)\n");
	splice(@S_MOVE,20);

	open(OUT,">$MAP_LOG_LIST") or &ERR2('LOG Œø Õ∏   œ¥.');
	print OUT @S_MOVE;
	close(OUT);

	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$kname ﬂΩœ¥.</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='∆ø¬¥'>
<br></form>
EOM

	&FOOTER;
	exit;
}

sub DEL2 {

&HOST_NAME;
	open(IN,"./charalog/main/$in{'filename'}") or &ERR2('   œ¥.');
	@CN_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);

			$dir2="./charalog/main";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/log";
			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/command";
			unlink("$dir2/$in{'filename'}");
&ADMIN_LOG("<font color=red>$kname ﬂΩœ¥. $host </font>");

	open(IN,"$DEF_LIST");
	@DEF_LIST = <IN>;
	close(IN);

	@NEW_DEF_LIST_DEL=();
	foreach(@DEF_LIST){
		($tid,$tname,$ttown_id,$ttown_flg,$tcon) = split(/<>/);
		if("$tid" eq "$kid"){
		}else{
			push(@NEW_DEF_LIST_DEL,"$_");
		}
	}
	open(OUT,">$DEF_LIST");
	print OUT @NEW_DEF_LIST_DEL;
	close(OUT);

	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$kname ﬂΩœ¥.</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='∆ø¬¥'>
<br></form>
EOM

	&FOOTER;
	exit;
}

sub ADMIN_LOG {

	if($lockkey) { &F_LOCK; }
	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
	&TIME_DATA;

	unshift(@A_LOG,"$_[0]($mday$hour$min)<BR>\n");
	splice(@A_LOG,20);

	open(OUT,">$ADMIN_LIST") or &ERR2('LOG Œø Õ∏   œ¥');
	print OUT @A_LOG;
	close(OUT);
	if (-e $lockfile) { unlink($lockfile); }
}


sub INIT_DATA {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("–Ω  $num ");}

	require "reset.cgi";
	&RESET_MODE;
&HOST_NAME;

	&ADMIN_LOG("Õ∏  ±»≠ﬂΩœ¥.[$host]");
	
	&HEADER;
	print <<"EOM";
<h2><font color=red>Õ∏  ±»≠ﬂΩœ¥.</h2></font>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='∆ø¬¥'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

# [ﬂ∞]  CHANGE2 ‘º
sub CHANGE2 {
	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){ &ERR2("ID, –Ω "); }

    #  
    my $file = $in{'fileno'};
    my $dir = "./charalog/main";
    
    #   (CHANGE ‘º “∑  )
    my $new_data = "$in{'eid'}<>$in{'epass'}<>$in{'ename'}<>$in{'echara'}<>$in{'estr'}<>$in{'eint'}<>$in{'elea'}<>$in{'echa'}<>$in{'esol'}<>$in{'egat'}<>$in{'econ'}<>$in{'egold'}<>$in{'erice'}<>$in{'ecex'}<>$in{'eclass'}<>$in{'earm'}<>$in{'ebook'}<>$in{'ebank'}<>$in{'esub1'}<>$in{'esub2'}<>$in{'epos'}<>$in{'emes'}<>$in{'ehost'}<>$in{'edate'}<>$in{'email'}<>$in{'eos'}<>$in{'eskill'}<>$in{'epoint'}<>$in{'ect'}<>$in{'elevel'}<>$in{'eexp'}<>$in{'ecodea'}<>$in{'ecodeb'}<>$in{'eqpoint'}<>\n";

    open(OUT, ">$dir/$file") or &ERR2("   œ¥.");
    print OUT $new_data;
    close(OUT);

    &HEADER;
    print <<EOM;
<center><h2>Õ∞ «æœ¥.</h2><br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='∆ø¬¥'>
</form>
</center>
EOM
    &FOOTER;
    exit;
}

# [ﬂ∞]  GG ‘º ()
sub GG {
    if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){ &ERR2(" œ¥."); }
    
    my $file = $in{'fileno'};
    my $dir = "./charalog/main";
    
    if(open(IN, "$dir/$file")) {
        my @lines = <IN>;
        close(IN);
        my @dt = split(/<>/, $lines[0]);
        $dt[25] = 1; # eos  1 
        
        open(OUT, ">$dir/$file");
        print OUT join('<>', @dt);
        close(OUT);
    }

    &HEADER;
    print <<EOM;
<center><h2> √≥ «æœ¥.</h2>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='∆ø¬¥'>
</form>
</center>
EOM
    &FOOTER;
    exit;
}

# [ﬂ∞]  GG1 ‘º ()
sub GG1 {
    if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){ &ERR2(" œ¥."); }
    
    my $file = $in{'fileno'};
    my $dir = "./charalog/main";
    
    if(open(IN, "$dir/$file")) {
        my @lines = <IN>;
        close(IN);
        my @dt = split(/<>/, $lines[0]);
        $dt[25] = 0; # eos  0  (/)
        
        open(OUT, ">$dir/$file");
        print OUT join('<>', @dt);
        close(OUT);
    }

    &HEADER;
    print <<EOM;
<center><h2> ( ) «æœ¥.</h2>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='∆ø¬¥'>
</form>
</center>
EOM
    &FOOTER;
    exit;
}

# [ﬂ∞]  CHANGE1 ‘º (ŒøÓøµ⁄)
sub CHANGE1 {
    &CHANGE; 
}


# -----------------------------------------------------
# BOT ADMIN UI (added)
# - configure bot counts and seed country names/capitals
# - stored in ./log_file/bot_admin.cfg
# -----------------------------------------------------

# --- BOT diplo helper (added) ---
sub BOT_DIPLO_KEY {
    my ($a,$b)=@_;
    $a=int($a||0); $b=int($b||0);
    return ($a<$b) ? "$a<>$b" : "$b<>$a";
}
sub BOT_DIPLO_LOAD {
    my %d=();
    my $f='./log_file/bot_diplo.dat';
    if (open(my $IN,$f)) {
        while(my $l=<$IN>) {
            chomp($l);
            next if ($l =~ /^\s*#/ || $l eq '');
            my ($a,$b,$st,$until)=split(/<>/,$l,4);
            my $k=&BOT_DIPLO_KEY($a,$b);
            $d{$k}={a=>int($a), b=>int($b), st=>($st||'WAR'), until=>int($until||0)};
        }
        close($IN);
    }
    return %d;
}

sub BOT_ADMIN {
    if(!(($in{'id'} eq "$adminid" && $in{'pass'} eq "$adminpass") || ($in{'id'} eq "$adminid2" && $in{'pass'} eq "$adminpass2") || ($in{'id'} eq "$adminid3" && $in{'pass'} eq "$adminpass3"))){
        &ERR2("NO AUTH");
    }

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

    my $bot_total = $cfg{'bot_total'} || 9;
    my $bot_per_country = $cfg{'bot_per_country'} || "3,3,3";
    my $seed_country_names = $cfg{'seed_country_names'} || "";
    my $seed_capitals = $cfg{'seed_capitals'} || "0,1,2";
    my $seed_elements = $cfg{'seed_elements'} || "1,2,3";

    # Personality sliders / diplomacy (added)
    my $bot_aggression = $cfg{'bot_aggression'}; if ($bot_aggression eq '') { $bot_aggression = 60; }
    my $bot_internal   = $cfg{'bot_internal'};   if ($bot_internal   eq '') { $bot_internal   = 50; }
    my $bot_defense    = $cfg{'bot_defense'};    if ($bot_defense    eq '') { $bot_defense    = 50; }
    my $bot_diplomacy  = $cfg{'bot_diplomacy'};  if ($bot_diplomacy  eq '') { $bot_diplomacy  = 40; }
    my $bot_diplo_enable = $cfg{'bot_diplo_enable'}; if ($bot_diplo_enable eq '') { $bot_diplo_enable = 1; }

    # Bot editor / scale (added)
    my $bot_force_country = $cfg{'bot_force_country'}; if ($bot_force_country eq '') { $bot_force_country = 0; }
    my $bot_scale = $cfg{'bot_scale'}; if ($bot_scale eq '') { $bot_scale = 100; }
    my $bot_stat_min = $cfg{'bot_stat_min'}; if ($bot_stat_min eq '') { $bot_stat_min = 40; }
    my $bot_stat_max = $cfg{'bot_stat_max'}; if ($bot_stat_max eq '') { $bot_stat_max = 70; }

    &HEADER;
    print <<"EOM";
<hr size=0><CENTER><font size=4><b>-- BOT Í¥Î¶¨Ïûê --</b></font><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BOT_ADMIN_SAVE>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><tbody bgcolor=$TD_C4>
<tr><th colspan=2>Î¥/ÍµÍ∞ ûêèôÑ∏åÖ</th></tr>

<tr><th width=25%>Î¥ Ï¥ùÏàò(Ï∞∏Í≥†)</th><td>
<input type=text name=bot_total size=6 value="$bot_total">
<br><small>ã§†ú ÉùÑ± àòäî "ÍµÍ∞Î≥ Î¥ àò" ï©Í≥ÑÎ Ç¨ö©ï©ãàã§.</small>
</td></tr>

<tr><th>ÍµÍ∞Î≥ Î¥ àò</th><td>
<input type=text name=bot_per_country size=30 value="$bot_per_country">
<br><small>òà: 3,3,3 (1ÍµÍ∞,2ÍµÍ∞,3ÍµÍ∞... àúÑú)</small>
</td></tr>

<tr><th>ãúìú ÍµÍ∞Î™</th><td>
<input type=text name=seed_country_names size=50 value="$seed_country_names">
<br><small>ÎπÑÏö∞Î© Í∏∞Ï°¥(WEI/SHU/WU) ú†Ïß. ûÖ†• ãú Î¥ Í±¥Íµ≠/Ï¥àÍ∏∞ ÍµÍ∞Î™ÖÏóê Ç¨ö©(Í∞ ÍµÍ∞Î™ÖÏ ÏµúÏÜå 4Í∏ûê ûêèô Î≥¥Ï†ï).</small>
</td></tr>

<tr><th>àòèÑ(èÑãú index)</th><td>
<input type=text name=seed_capitals size=30 value="$seed_capitals">
<br><small>òà: 0,1,2 (Í∞ ÍµÍ∞ àòèÑ èÑãú ù∏ç±ä§)</small>
</td></tr>

<tr><th>ÜçÑ±(Ñ†Éù)</th><td>
<input type=text name=seed_elements size=30 value="$seed_elements">
<br><small>òà: 1,2,3</small>
</td></tr>

<tr><th colspan=2>Î¥ óêîîÑ∞ / Í∑úÎ™®</th></tr>

<tr><th>Î¥ ÍµÍ∞ Í∞ïÏ†ú</th><td>
<input type=text name=bot_force_country size=6 value="$bot_force_country">
<br><small>0ù¥Î© ûêèô(ãúìú ÍµÍ∞Î≥). äπ†ï ÍµÍ∞Î≤àÌò∏Î• ûÖ†•ïòÎ© <b>Î™®Îì† Î¥áÏùÑ Í∑ ÍµÍ∞Î° Í∞ïÏ†ú Î∞∞Ï†ï</b>ï©ãàã§.</small>
</td></tr>

<tr><th>Î¥ Í∑úÎ™®(Ï¥àÍ∏∞ ûêõê)</th><td>
<input type=range name=bot_scale min=10 max=500 value="$bot_scale" oninput="document.getElementById('v_sc').innerHTML=this.value;"> <b id='v_sc'>$bot_scale</b>%
<br><small>Ï¥àÍ∏∞ Gold/Riceóê Î∞∞Ïú® †Åö©(Í∏∞Î≥∏ 100%).</small>
</td></tr>

<tr><th>Î¥ ä•†•Ïπ Î≤îÏúÑ</th><td>
min <input type=text name=bot_stat_min size=4 value="$bot_stat_min">  max <input type=text name=bot_stat_max size=4 value="$bot_stat_max">
<br><small>Î¨¥Î†•/Ïß†•/ÜµÜî/Îß§Î†•ùò ûúç§ Î≤îÏúÑ(ï© 200 Ç¥óêÑú Î≥¥Ï†ï). òà: 40~70</small>
</td></tr>

<tr><th colspan=2>Î¥ Ñ±ñ•(†Ñó≠)</th></tr>

<tr><th>Í≥µÍ≤©Ñ±</th><td>
<input type=range name=bot_aggression min=0 max=100 value="$bot_aggression" oninput="document.getElementById('v_ag').innerHTML=this.value;">
 <b id='v_ag'>$bot_aggression</b>
<br><small>ÜíùÑàòÎ° Í≥µÍ≤©/õê†ï ÎπàÎèÑÜë, Í≥µÍ≤© Í∞úÏãú Ï°∞Í±¥ ôÑôî</small>
</td></tr>

<tr><th>Ç¥†ïÑ±</th><td>
<input type=range name=bot_internal min=0 max=100 value="$bot_internal" oninput="document.getElementById('v_in').innerHTML=this.value;">
 <b id='v_in'>$bot_internal</b>
<br><small>ÜíùÑàòÎ° ÏπòÏïà/Ç¥†ï ö∞Ñ†Üë (ÏπòÏïà Í∏∞ÏÑ† ÉÅäπ)</small>
</td></tr>

<tr><th>àòÎπÑÏÑ±</th><td>
<input type=range name=bot_defense min=0 max=100 value="$bot_defense" oninput="document.getElementById('v_df').innerHTML=this.value;">
 <b id='v_df'>$bot_defense</b>
<br><small>ÜíùÑàòÎ° Ñ±Î≤/àòÎπ ö∞Ñ†Üë (Ñ±Î≤ Î∂Ï° ûÑÍ≥ÑÏπò ÉÅäπ)</small>
</td></tr>

<tr><th>ô∏ÍµêÏÑ±</th><td>
<input type=range name=bot_diplomacy min=0 max=100 value="$bot_diplomacy" oninput="document.getElementById('v_dp').innerHTML=this.value;">
 <b id='v_dp'>$bot_diplomacy</b>
<br><small>ÜíùÑàòÎ° èôÎß/ú¥†Ñ ÎπàÎèÑÜë (Î¥ †Ñö© ô∏Íµ †àù¥ñ¥)</small>
<br><label><input type=checkbox name=bot_diplo_enable value=1 @{[ $bot_diplo_enable ? 'checked' : '' ]}> Î¥ ô∏Íµ ûêèôôî Ç¨ö©</label>
</td></tr>

<tr><th>†Åö©</th><td>
<label><input type=checkbox name=reset_setup value=1> ã§ùå Ñ¥óê Î¥/ÍµÍ∞ ûêèôÑ∏åÖ ã§ãú ã§ñâ(Í∏∞Ï°¥ bot_setup.done Ç≠†ú)</label>
</td></tr>

<tr><th colspan=2>
<input type=submit value="û•">
</th></tr>
</tbody></table>
</form>

<div style="width:80%; margin-top:12px; text-align:left;">
<b>Ï∞∏Í≥†</b><br>
- Î¥ AIäî Ç¥†ï/àòÎπ/Í≥µÍ≤©ùÑ ûêèô Ñ†ÉùïòÍ≥, ù∏†ë èÑãú Ï§ Í≤üÏùÑ †êàòôîï¥ Í≥µÍ≤©ï©ãàã§.<br>
- (Ï∂îÍ) Í≥µÍ≤©Ñ±ù¥ ÜíúºÎ© †ÑÑ†ù¥ óÜñ¥èÑ õê†ïïòÎ©, ô∏Íµ ûêèôôîÍ∞ ÏºúÏ†∏ ûàúºÎ© èôÎß/ú¥†ÑÍµ Í≥µÍ≤© Í≤üÏóêÑú †úô∏ê©ãàã§.<br>
- Î¥áÏù¥ Í±¥Íµ≠ï† ïå ÍµÎ™ÖÏ ÏµúÏÜå 4Í∏ûê ù¥ÉÅù¥ êòèÑÎ° ûêèôúºÎ° Î≥¥Ï†ïê©ãàã§.<br>
</div>

<hr size=0><CENTER><font size=3><b>-- Ñ¥ Í∞ïÏ†ú ÏßÑÌñâ(Öåä§ä∏/ö¥òÅ) --</b></font><hr size=0>
<div style="width:80%; text-align:left; margin:0 auto;">
<form method="post" action="dkajlfjeioaefhoiwqhfeouihwefwefksdjklfjwe.cgi">
<input type=hidden name=turn_force value=1>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
ÏßÑÌñâ Ñ¥àò: <select name=turn_n>
<option value=1>1</option><option value=2>2</option><option value=3>3</option><option value=4>4</option><option value=5>5</option>
<option value=6>6</option><option value=7>7</option><option value=8>8</option><option value=9>9</option><option value=10>10</option>
<option value=15>15</option><option value=20>20</option><option value=25>25</option><option value=30 selected>30</option>
</select>

<label style="margin-left:12px;"><input type="checkbox" name="stop_elim" value="1"> ∆Ø¡§ ±π∞° ∏Í∏¡Ω√ ¡ﬂ¡ˆ</label>
CID: <input type="text" name="stop_cid" value="" style="width:50px;">
<input type=submit value="Ñ†Éùïú Ñ¥ Í∞ïÏ†ú ÏßÑÌñâ">
<small> Í¥Î¶¨ÏûêÎß èôûë, ïú Î≤àÏùò öîÏ≤úºÎ° ÏµúÎ 30Ñ¥ÍπåÏ ó∞Üç Ï≤òÎ¶¨.</small>
</form>
</div>
EOM
}



# ------------------------------------------------------------------
# BOT per-country personality / strategy presets / diplomacy monitor (added)
# ------------------------------------------------------------------


# --- Country list for per-country settings ---
my @COUL = ();
if (open(my $CIN2, "$COUNTRY_LIST")) { @COUL = <$CIN2>; close($CIN2); }
my @CIDS = ();
my %CNAME = ();
foreach my $cl (@COUL) {
    chomp($cl);
    next if $cl eq '';
    my ($cid,$cname) = split(/<>/, $cl);
    $cid = int($cid||0);
    next if $cid <= 0;
    push(@CIDS, $cid);
    $CNAME{$cid} = $cname;
}

# Global strategy preset
my $bot_strategy = $cfg{'bot_strategy'}; if ($bot_strategy eq '') { $bot_strategy = 'BALANCED'; }

print "<hr size=0><CENTER><font size=3><b>-- BOT Ñ±ñ•(ÍµÍ∞Î≥) / †Ñûµ îÑÎ¶¨ÏÖã --</b></font><hr size=0>";
print "<form method=post action=admin.cgi>";
print "<input type=hidden name=mode value=BOT_ADMIN_SAVE>";
print "<input type=hidden name=id value=\"$in{id}\">";
print "<input type=hidden name=pass value=\"$in{pass}\">";

print "<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><tbody bgcolor=$TD_C4>";
print "<tr><th colspan=2>†Ñûµ îÑÎ¶¨ÏÖã(†Ñó≠)</th></tr>";
print "<tr><th width=25%>†Ñûµ</th><td>";
print "<select name=bot_strategy>";
my @PRE = ('BALANCED','TECH_FIRST','ECON_FIRST','CASTLE_WEAK','DIST_NEAR');
foreach my $p (@PRE) {
    my $sel = ($bot_strategy eq $p) ? 'selected' : '';
    print "<option value=\"$p\" $sel>$p</option>";
}
print "</select> ";
print "<small>Í≤ †êàòôî Í∞Ï§ëÏπò(Í∏∞Ïà†/Í≤ΩÏ†ú/Ñ±Î≤/Í±∞Î¶¨)Î• Î∞îÍøâãàã§.</small>";
print "</td></tr>";

print "<tr><th colspan=2>ÍµÍ∞Î≥ Ñ±ñ•/†Ñûµ</th></tr>";
print "<tr><th colspan=2><small>ÎπÑÏõåëêÎ© †Ñó≠ Ñ§†ïùÑ î∞Î¶ÖÎãàã§. Í∞ Î≤îÏúÑ 0~100.</small></th></tr>";

foreach my $cid (@CIDS) {
    my $tag = $CNAME{$cid}; if ($tag eq '') { $tag = "ÍµÍ∞$cid"; }
    my $ag = $cfg{"bot_aggression_c$cid"}; my $inl = $cfg{"bot_internal_c$cid"};
    my $df = $cfg{"bot_defense_c$cid"};    my $dp  = $cfg{"bot_diplomacy_c$cid"};
    my $st = $cfg{"bot_strategy_c$cid"};   if ($st eq '') { $st = ''; }

    print "<tr><th colspan=2 style=\"text-align:left; padding:6px;\">";
    print "[$cid] $tag</th></tr>";

    print "<tr><th>Í≥µÍ≤©/Ç¥†ï/àòÎπ/ô∏Íµ</th><td>";
    print "Í≥µÍ≤© <input type=text name=bot_aggression_c$cid size=3 value=\"$ag\"> ";
    print "Ç¥†ï <input type=text name=bot_internal_c$cid size=3 value=\"$inl\"> ";
    print "àòÎπ <input type=text name=bot_defense_c$cid size=3 value=\"$df\"> ";
    print "ô∏Íµ <input type=text name=bot_diplomacy_c$cid size=3 value=\"$dp\"> ";
    print "</td></tr>";

    print "<tr><th>†Ñûµ îÑÎ¶¨ÏÖã</th><td>";
    print "<select name=bot_strategy_c$cid>";
    print "<option value=\"\">[†Ñó≠ Ç¨ö©]</option>";
    foreach my $p (@PRE) {
        my $sel = ($st eq $p) ? 'selected' : '';
        print "<option value=\"$p\" $sel>$p</option>";
    }
    print "</select>";
    print "</td></tr>";
}

print "<tr><th colspan=2><input type=submit value=\"û•(ÍµÍ∞Î≥/†Ñûµ)\"></th></tr>";
print "</tbody></table>";
print "</form>";

# --- Diplomacy monitor / force-set ---
print "<hr size=0><CENTER><font size=3><b>-- BOT ô∏Íµ òÑô© / Í∞ïÏ†ú Ñ§†ï --</b></font><hr size=0>";
my %DIP = &BOT_DIPLO_LOAD();
print "<div style=\"width:80%; text-align:left; margin:0 auto;\"><small>";
print "- ïÑûò ô∏ÍµêÎäî <b>Î¥ †Ñö© †àù¥ñ¥</b>ù¥Î©, Î¥áÏùò Í≤ Ñ††ï/Í≥µÍ≤©óêÑúÎß Î∞òÏòÅê©ãàã§.<br>";
print "- TRUCEäî Í∏∞Í∞Ñù¥ ÅùÇòÎ© WARÎ° ûêèô Î≥µÍï©ãàã§.</small></div>";

print "<table width=80% cellspacing=1 border=0 bgcolor=$TABLE_C><tbody bgcolor=$TD_C4>";
print "<tr><th width=35%>Í¥Í≥</th><th width=15%>ÉÅÉú</th><th width=30%>ÎßåÎ£å</th><th width=20%>Ï°∞Ïûë</th></tr>";

my $now = time();
foreach my $k (sort keys %DIP) {
    my $a = $DIP{$k}->{a}; my $b = $DIP{$k}->{b};
    my $st = $DIP{$k}->{st}; my $until = int($DIP{$k}->{until}||0);
    my $an = $CNAME{$a}; if ($an eq '') { $an = "ÍµÍ∞$a"; }
    my $bn = $CNAME{$b}; if ($bn eq '') { $bn = "ÍµÍ∞$b"; }
    my $until_s = ($st eq 'TRUCE' && $until > 0) ? scalar(localtime($until)) : "-";
    print "<tr><td>$a:$an &nbsp;vs&nbsp; $b:$bn</td><td><b>$st</b></td><td>$until_s</td>";
    print "<td>";
    print "<form method=post action=admin.cgi style=\"display:inline;\">";
    print "<input type=hidden name=mode value=BOT_DIPLO_SET>";
    print "<input type=hidden name=id value=\"$in{id}\"><input type=hidden name=pass value=\"$in{pass}\">";
    print "<input type=hidden name=a value=\"$a\"><input type=hidden name=b value=\"$b\">";
    print "<select name=status>";
    foreach my $s ('WAR','TRUCE','ALLY') {
        my $sel = ($s eq $st) ? 'selected' : '';
        print "<option value=\"$s\" $sel>$s</option>";
    }
    print "</select> ";
    print "days <input type=text name=days size=3 value=\"7\"> ";
    print "<input type=submit value=\"†Åö©\">";
    print "</form>";
    print "</td></tr>";
}
print "</tbody></table>";

sub BOT_ADMIN_SAVE {
    if(!(($in{'id'} eq "$adminid" && $in{'pass'} eq "$adminpass") || ($in{'id'} eq "$adminid2" && $in{'pass'} eq "$adminpass2") || ($in{'id'} eq "$adminid3" && $in{'pass'} eq "$adminpass3"))){
        &ERR2("NO AUTH");
    }
    my $f = "./log_file/bot_admin.cfg";
    unless(-d "./log_file"){ mkdir("./log_file", 0777); }

    my $bot_total = $in{'bot_total'}; $bot_total =~ s/[^0-9]//g; if ($bot_total eq '') { $bot_total = 9; }
    my $bot_per_country = $in{'bot_per_country'}; $bot_per_country =~ s/[^0-9,\s]//g; if ($bot_per_country eq '') { $bot_per_country = "3,3,3"; }

    my $seed_country_names = $in{'seed_country_names'}; $seed_country_names =~ s/[\r\n]//g;
    my $seed_capitals = $in{'seed_capitals'}; $seed_capitals =~ s/[^0-9,\s]//g; if ($seed_capitals eq '') { $seed_capitals = "0,1,2"; }
    my $seed_elements = $in{'seed_elements'}; $seed_elements =~ s/[^0-9,\s]//g; if ($seed_elements eq '') { $seed_elements = "1,2,3"; }

    my $bot_aggression = $in{'bot_aggression'}; $bot_aggression =~ s/[^0-9]//g; if ($bot_aggression eq '') { $bot_aggression = 60; }
    my $bot_internal   = $in{'bot_internal'};   $bot_internal   =~ s/[^0-9]//g; if ($bot_internal   eq '') { $bot_internal   = 50; }
    my $bot_defense    = $in{'bot_defense'};    $bot_defense    =~ s/[^0-9]//g; if ($bot_defense    eq '') { $bot_defense    = 50; }
    my $bot_diplomacy  = $in{'bot_diplomacy'};  $bot_diplomacy  =~ s/[^0-9]//g; if ($bot_diplomacy  eq '') { $bot_diplomacy  = 40; }
    my $bot_diplo_enable = ($in{'bot_diplo_enable'} eq '1') ? 1 : 0;

    # Bot editor / scale (added)
    my $bot_force_country = $in{'bot_force_country'}; $bot_force_country =~ s/[^0-9]//g; if ($bot_force_country eq '') { $bot_force_country = 0; }
    my $bot_scale = $in{'bot_scale'}; $bot_scale =~ s/[^0-9]//g; if ($bot_scale eq '') { $bot_scale = 100; }
    if ($bot_scale < 10) { $bot_scale = 10; }
    if ($bot_scale > 500) { $bot_scale = 500; }
    my $bot_stat_min = $in{'bot_stat_min'}; $bot_stat_min =~ s/[^0-9]//g; if ($bot_stat_min eq '') { $bot_stat_min = 40; }
    my $bot_stat_max = $in{'bot_stat_max'}; $bot_stat_max =~ s/[^0-9]//g; if ($bot_stat_max eq '') { $bot_stat_max = 70; }
    if ($bot_stat_min < 1) { $bot_stat_min = 1; }
    if ($bot_stat_max < $bot_stat_min) { $bot_stat_max = $bot_stat_min; }
    if ($bot_stat_max > 200) { $bot_stat_max = 200; }

    if ($bot_aggression > 100) { $bot_aggression = 100; }
    if ($bot_internal   > 100) { $bot_internal   = 100; }
    if ($bot_defense    > 100) { $bot_defense    = 100; }
    if ($bot_diplomacy  > 100) { $bot_diplomacy  = 100; }


my $bot_strategy = $in{'bot_strategy'}; $bot_strategy =~ s/[^A-Z_]//g; if ($bot_strategy eq '') { $bot_strategy = 'BALANCED'; }

# Load old cfg to preserve unknown/per-country keys
my %old = ();
if (open(my $OIN, $f)) {
    while(my $l = <$OIN>) {
        chomp($l);
        next if ($l =~ /^\s*#/ || $l eq "");
        my ($k,$v) = split(/<>/, $l, 2);
        $old{$k} = $v;
    }
    close($OIN);
}

# Per-country overrides: read countries from COUNTRY_LIST
my @COUL = ();
if (open(my $CIN2, "$COUNTRY_LIST")) { @COUL = <$CIN2>; close($CIN2); }
my @CIDS = ();
foreach my $cl (@COUL) {
    chomp($cl);
    next if $cl eq '';
    my ($cid) = split(/<>/, $cl);
    $cid = int($cid||0);
    next if $cid <= 0;
    push(@CIDS, $cid);
}

foreach my $cid (@CIDS) {
    my $k1 = "bot_aggression_c$cid"; if (defined $in{$k1} && $in{$k1} ne '') { my $v=$in{$k1}; $v =~ s/[^0-9]//g; if ($v ne '') { if ($v>100){$v=100;} $old{$k1}=$v; } }
    my $k2 = "bot_internal_c$cid";   if (defined $in{$k2} && $in{$k2} ne '') { my $v=$in{$k2}; $v =~ s/[^0-9]//g; if ($v ne '') { if ($v>100){$v=100;} $old{$k2}=$v; } }
    my $k3 = "bot_defense_c$cid";    if (defined $in{$k3} && $in{$k3} ne '') { my $v=$in{$k3}; $v =~ s/[^0-9]//g; if ($v ne '') { if ($v>100){$v=100;} $old{$k3}=$v; } }
    my $k4 = "bot_diplomacy_c$cid";  if (defined $in{$k4} && $in{$k4} ne '') { my $v=$in{$k4}; $v =~ s/[^0-9]//g; if ($v ne '') { if ($v>100){$v=100;} $old{$k4}=$v; } }
    my $ks = "bot_strategy_c$cid";   if (defined $in{$ks}) { my $v=$in{$ks}; $v =~ s/[^A-Z_]//g; $old{$ks}=$v; } # empty ok
}

$old{'bot_strategy'} = $bot_strategy;

    if (open(my $OUT, ">$f")) {

# write base keys
print $OUT "bot_total<>$bot_total\n";
print $OUT "bot_per_country<>$bot_per_country\n";
print $OUT "seed_country_names<>$seed_country_names\n";
print $OUT "seed_capitals<>$seed_capitals\n";
print $OUT "seed_elements<>$seed_elements\n";
print $OUT "bot_force_country<>$bot_force_country\n";
print $OUT "bot_scale<>$bot_scale\n";
print $OUT "bot_stat_min<>$bot_stat_min\n";
print $OUT "bot_stat_max<>$bot_stat_max\n";
print $OUT "bot_aggression<>$bot_aggression\n";
print $OUT "bot_internal<>$bot_internal\n";
print $OUT "bot_defense<>$bot_defense\n";
print $OUT "bot_diplomacy<>$bot_diplomacy\n";
print $OUT "bot_diplo_enable<>$bot_diplo_enable\n";
print $OUT "bot_strategy<>$old{'bot_strategy'}\n";

# preserve per-country and any other existing keys (added)
foreach my $k (sort keys %old) {
    next if ($k eq 'bot_total' || $k eq 'bot_per_country' || $k eq 'seed_country_names' || $k eq 'seed_capitals' || $k eq 'seed_elements' ||
             $k eq 'bot_force_country' || $k eq 'bot_scale' || $k eq 'bot_stat_min' || $k eq 'bot_stat_max' ||
             $k eq 'bot_aggression' || $k eq 'bot_internal' || $k eq 'bot_defense' || $k eq 'bot_diplomacy' || $k eq 'bot_diplo_enable' || $k eq 'bot_strategy');
    my $v = $old{$k};
    $v =~ s/[\r\n]//g;
    print $OUT "$k<>$v\n";
}

        close($OUT);
        chmod(0666, $f);
    }

    if ($in{'reset_setup'} eq '1') {
        unlink("./log_file/bot_setup.done");
    }

    &HEADER;
    print "<hr><center>û• ôÑÎ£. <a href=admin.cgi?id=$in{id}&pass=$in{pass}>Í¥Î¶¨Ïûê Î©îÏù∏úºÎ°</a></center>";
}

1;