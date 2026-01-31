#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR2("로딩중입니다. 잠시만 기다려 주세요."); }
&DECODE;
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("주소바에 값을 입력하지 말아주세요."); }
if($mode eq 'STATUS') { &STATUS; }
else { &ERR("올바르지 않은 액세스입니다."); }


sub STATUS {

	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");
	&CHARA_ITEM_OPEN;
	&MAKE_GUEST_LIST;
	&HOST_NAME;
	&TIME_DATA;



	opendir(dirlist,"./charalog/main");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"./charalog/main/$file")){
				&ERR2("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);


	$nam = 0;
	foreach(@CL_DATA){
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/);
		($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex,$ebo_ex,$egi_ex,$ech_ex,$egu_ex,$ego_ex,$ejin_ex) = split(/,/,$esub1);
		
		if($kid eq $eid){
			$ehost = "$host";
			&ENEMY_INPUT;
		}

		# 동일 호스트 차단 로직 주석 처리 시작
		# if($kid ne $eid && $khost eq $ehost){
		# 	$eos = 0;
		# 	&ENEMY_INPUT;
		# 	$kos = 0;
		# 	&CHARA_MAIN_INPUT;
		# }
		# 주석 처리 끝

		if($ejin_ex == 1){
			$nam++;
		}
	} # foreach를 닫는 괄호




	open(IN,"./log_file/event_on.cgi");
	@EVENT = <IN>;
	close(IN);

	($eventon,$emoney,$etime) = split(/<>/,$EVENT[0]);

		$event_limit_time = int(($etime + 3600 - $tt) / 60);

		if($etime+3600 < $tt && $eventon == 1){
			$eventon = 2;
		}

	@EVENT_DATA=();
	unshift(@EVENT_DATA,"$eventon<>$emoney<>$etime<>");
	open(OUT,">./log_file/event_on.cgi") or &ERR('MAIN 새로운 데이터를 기입할 수 없습니다.');
	print OUT @EVENT_DATA;
	close(OUT);

		if($eventon == 1){
			$event_select = "<table cellpadding=0 cellspacing=0><tr><form action=./event.cgi method=post><td><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=TOP_NEW><input type=image src=$IMG/event_entry.jpg></td></form></tr><tr><td bgcolor=black><b>총상금</b>:$emoney<br><b>개시</b> $event_limit_time분전</td></tr></table>";
		}elsif($eventon == 2){
			$event_select = "<table cellpadding=0 cellspacing=0><tr><form action=./event.cgi method=post><td><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=image src=$IMG/event_start.jpg></td></form></tr><tr><td bgcolor=black><b>총상금</b>:$emoney<br><b>생존자</b>:$nam명</td></tr></table>";
		}

	$levelup = int(200 * (1+($klevel*0.1)));

	($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex) = split(/,/,$ksub1);

	if($go_ex < 500){
		$sangtae = "건강";
	}elsif($go_ex <1000 && $go_ex > 499){
		$sangtae = "보통";
	}elsif($go_ex < 1250 && $go_ex > 999){
		$sangtae = "나태";
	}elsif($go_ex < 1500 && $go_ex > 1249){
		$sangtae = "중태";
	}elsif($go_ex <1700 && $go_ex > 1499){
		$sangtae = "위험";
	}







	if($kos ne 1){
		&ERR2("<img src=$IMG/injeung.jpg>");
	}
	open(IN,"./log_file/date_count.cgi") or &ERR('파일을 열지 않았습니다.');
	@MONTH_DATA = <IN>;
	close(IN);





	if($mmonth < 4){
		$bg_c = "#FFFFFF";
	}elsif($mmonth < 7){
		$bg_c = "#FFE0E0";
	}elsif($mmonth < 10){
		$bg_c = "#60AF60";
	}else{
		$bg_c = "#884422";
	}

	($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
	$new_date = sprintf("%02d\년%02d\월", $F_YEAR+$myear, $mmonth);




	$townnum=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro,$z2nou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy,$zzsouba,$zzdef_att,$zzsub1,$zzsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zzname1,$zzname2,$zzbong1,$zzbong2,$zzbong3)=split(/<>/);
		if($kpos eq $townnum){
			if($kid eq "$zzbong1" ){
				$townnum1 = "$zzbong1";
			}elsif($kid eq "$zzbong2"){
				$townnum1 = "$zzbong2";
			}elsif($kid eq "$zzbong3"){
				$townnum1 = "$zzbong3";
			}
		}
		$townnum++;

		if($kid eq "$zzbong1" || $kid eq "$zzbong2" || $kid eq "$zzbong3"){
		$bongt = "<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=BONGTOG><input type=hidden name=bongid value=$kid><input type=hidden name=bongtown value=$z2name><input type=hidden name=bongname value=$kname><input type=hidden name=bongimg value=$kchara><input type=image ALT=$kname님의 봉토게시판입니다. src=\"$IMG/bongto1.jpg\">";
		}


		if($z2con eq $kcon){
				$zsyo_sal += int($z2syo * 8 * $z2num / 16000);
				$znou_sal += int($z2nou * 8 * $z2num / 16000);
		}
	}

	if($xking eq "$kid"){
		$rank_mes = "군주";
	}elsif($x0 eq "$kid"){
		$rank_mes = "참모";
	}elsif($x1 eq "$kid"){
		$rank_mes = "대장군";
	}elsif($x2 eq "$kid"){
		$rank_mes = "표기장군";
	}elsif($x3 eq "$kid"){
		$rank_mes = "거기장군";
	}elsif($x4 eq "$kid"){
		$rank_mes = "위장군";
	}elsif($x5 eq "$kid"){
		$rank_mes = "정동장군";
	}elsif($x6 eq "$kid"){
		$rank_mes = "정서장군";
	}elsif($x7 eq "$kid"){
		$rank_mes = "정남장군";
	}elsif($x8 eq "$kid"){
		$rank_mes = "정북장군";
	}elsif($x9 eq "$kid"){
		$rank_mes = "진동장군";
	}elsif($x10 eq "$kid"){
		$rank_mes = "진서장군";
	}elsif($x11 eq "$kid"){
		$rank_mes = "진남장군";
	}elsif($x12 eq "$kid"){
		$rank_mes = "진북장군";
	}elsif($x13 eq "$kid"){
		$rank_mes = "안동장군";
	}elsif($x14 eq "$kid"){
		$rank_mes = "안서장군";
	}elsif($x15 eq "$kid"){
		$rank_mes = "안남장군";
	}elsif($x16 eq "$kid"){
		$rank_mes = "안북장군";
	}elsif($x17 eq "$kid"){
		$rank_mes = "승상";
	}elsif($x18 eq "$kid"){
		$rank_mes = "태부";
	}elsif($x19 eq "$kid"){
		$rank_mes = "태사";
	}elsif($x20 eq "$kid"){
		$rank_mes = "태보";
	}elsif($x21 eq "$kid"){
		$rank_mes = "어사대부";
	}elsif($x22 eq "$kid"){
		$rank_mes = "태위";
	}elsif($x23 eq "$kid"){
		$rank_mes = "이부상서";
	}elsif($x24 eq "$kid"){
		$rank_mes = "호부상서";
	}elsif($x25 eq "$kid"){
		$rank_mes = "예부상서";
	}elsif($x26 eq "$kid"){
		$rank_mes = "병부상서";
	}else{$rank_mes = "장수";
	}

	if($zdef_att< 200){
	$def_nums = 2;
	}
	if($zdef_att< 400){
	if($zdef_att>200){
	$def_nums = 3;}
	}
	if($zdef_att< 600){
	if($zdef_att>400){
	$def_nums = 4;}
	}
	if($zdef_att< 800){
	if($zdef_att>600){
	$def_nums = 5;}
	}
	if($zdef_att < 1001){
	if($zdef_att>800){
	$def_nums = 6;}
	}


	if($kclass > 10000){
		$dok = "<option style=color:#000000;background-color:#CCCCCC; value=48>독립(민심영향)";
	}
	if($xking eq $kid || $x0 eq $kid){
		$add_com .= "<option style=color:#000000;background-color:#CCCCCC; value=32>도시초토화(군주,참모 전용 금 500, 계급치 20% 소모)";
	}

	if($cou_name[$kcon] eq "" || $kcon == 0 && $xmark < $BATTLE_STOP){
		$add_com .= "<option style=color:#000000;background-color:#CCCCCC; value=21>임관";
	}
	if($cou_name[$kcon] ne ""){
		$add_com .= "<option style=color:#000000;background-color:#CCCCCC; value=40>하야";
	}

	if($kpos == $kct || $townnum1 eq "$kid"){
		$add_com1 ="<option style=color:#000000;background-color:#CCCCCC; value=>===================== 자택 =====================<option style=color:#000000;background-color:#CCCCCC; value=43>수색(매력영향)<option style=color:#000000;background-color:#CCCCCC; value=26>능력수련(무료)";
	}

	if($zshiro > 32000){
		$sungru = "sungru4";
	}elsif($zshiro > 24000){
		$sungru = "sungru3";
	}elsif($zshiro > 15000){
		$sungru = "sungru2";
	}elsif($zshiro == 0){
		$sungru = "sungzero";
	}else{
		$sungru = "sungru1";
	}
	


	open(IN,"$UNIT_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
	@UNI_DATA = <IN>;
	close(IN);

	open(IN,"$TRAP_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
	@TRAP_DATA = <IN>;
	close(IN);

	$uhit=0;
	$unit_num=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if("$uid" eq "$kid"){$uhit=1;last;}
		if($unit_id eq $kid && $uid ne $unit_id){
		$unit_num++;
		}
	}
	$unit_num1 = $unit_num*30;
	if(!$uhit){
		$unit_id="";
		$uunit_name="없음";
	}
	if($unit_id eq $kid){
		$add_com .= "<option style=color:#000000;background-color:#CCCCCC; value=28>집합(부대장전용 금 $unit_num1)<option style=color:#000000;background-color:#CCCCCC; value=53>발령(부대장전용)";
	}


	if($xking eq $kid){
		$add_com .= "<option style=color:#000000;background-color:#CCCCCC; value=46>왕위계승";
	}

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<9){$S_MES .= " $S_MOVE[$p]<BR>";$p++;}

	open(IN,"./charalog/log/$kid.cgi");
	@LOG_DATA = <IN>;
	close(IN);
	$p=0;
	while($p<15){$log_list .= "<font color=navy>●</font>$LOG_DATA[$p]<BR>";$p++;}


	open(IN,"./charalog/log2/$kid.cgi");
	@LOG_DATA1 = <IN>;
	close(IN);
	$p=0;
	while($p<15){$log_list1 .= "<font color=navy>●</font>$LOG_DATA1[$p]<BR>";$p++;}

	open(IN,"./charalog/log3/$kid.cgi");
	@LOG_DATA2 = <IN>;
	close(IN);
	$p=0;
	while($p<15){$log_list2 .= "<font color=navy>●</font>$LOG_DATA2[$p]<BR>";$p++;}

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$wyear = $myear+$F_YEAR;
	if($mtime > $kdate){
		$wmonth = $mmonth;
		if($wmonth > 12){
			$wyear++;
			$wmonth = 1;
		}
	}else{
		$wmonth = $mmonth;
	}

	for($i=0;$i<$MAX_COM;$i++){
		($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/,$COM_DATA[$i]);
		$no = $i+1;
		if($cid eq ""){
			$com_list .= "<TR height=20><TH width=15%>$no턴</TH><TH width=30%>$wyear년 $wmonth월</TH><TH> - </TH></TR>";
		}else{
			$com_list .= "<TR height=20><TH width=15%>$no턴</TH><TH width=30%>$wyear년 $wmonth월</TH><TH>$cname</TH></TR>";
		}
		$wmonth++;
		if($wmonth > 12){
			$wyear++;
			$wmonth = 1;
		}
	}

	open(IN,"$DEF_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
	@DEF_DATA = <IN>;
	close(IN);
	

	$def_num=0;
	foreach(@DEF_DATA){
		($did,$dname,$dtown_id,$dtown_flg,$dcon,$dchara,$dsol,$dsub1_ex,$dtown_battle,$ddef)=split(/<>/);
		if($kpos eq $dtown_id){
			$def_num++;




			if($dsub1_ex == 0 || $dsub1_ex == 1 || $dsub1_ex == 3 || $dsub1_ex == 9 || $dsub1_ex == 13 || $dsub1_ex == 19  || $dsub1_ex == 20 || $dsub1_ex == 21 || $dsub1_ex == 23 || $dsub1_ex == 26 || $dsub1_ex == 27 || $dsub1_ex == 28){
				$djong = 1;
			}elsif($dsub1_ex == 4 || $dsub1_ex == 8 || $dsub1_ex == 10 || $dsub1_ex == 11 || $dsub1_ex == 22 || $dsub1_ex == 24 || $dsub1_ex == 25){
				$djong = 2;
			}elsif($dsub1_ex == 2 || $dsub1_ex == 16 || $dsub1_ex == 15 || $dsub1_ex == 6  || $dsub1_ex == 18 || $dsub1_ex == 29){
				$djong = 3;
			}elsif($dsub1_ex == 5 || $dsub1_ex == 7 || $dsub1_ex == 12 || $dsub1_ex == 17 || $dsub1_ex == 30){
				$djong = 4;
			}



			if($dtown_battle){
				$dsolmark = "sungbattle";
			}else{

			if(1000 > $dsol){
				$dsolmark = "sung1";
			}elsif(1500 > $dsol){
				$dsolmark = "sung2";
			}elsif(2500 > $dsol){
				$dsolmark = "sung3";
			}else{
				$dsolmark = "sung4";
			}

			}
			$kkk = "<img hint=\"<table align=center cellpadding=0 cellspacing=0 width=93%><tr><td width=66><img src=\'$IMG/$dchara.gif\'></td><td width=120><p><span style=font-size:9pt;><b>$cou_name[$dcon]국<br>$dname부대</b><br>$SOL_TYPE[$dsub1_ex] $dsol명<br><font color=red>$ddef명째 방어중</span></font></p></td></tr></table>\" src=\"$IMG/$dsolmark$djong.gif\" border=0>";
			if($def_num eq 1){
			$def_list1 = "$kkk";	
			}
			if($def_num eq 2){
			$def_list2 = "$kkk";
			}
			if($def_num eq 3){
			$def_list3 = "$kkk";
			}
			if($def_num eq 4){
			$def_list4 = "$kkk";
			}
			if($def_num eq 5){
			$def_list5 = "$kkk";
			}
			if($def_num eq 6){
			$def_list6 = "$kkk";
			}

		}
	}

	open(IN,"$TRAP_LIST") or &ERR("지정된 파일이 열리지 않습니다.");
	@TRAP_DATA = <IN>;
	close(IN);

	@trapstr = ("","화계","낙석","허보");
	foreach(@TRAP_DATA){
		($ttid,$ttname,$tttown_id,$ttcon,$tttrap,$ttint)=split(/<>/);
		if($kpos eq $tttown_id){
			$trap_list .= "<td width=133><center><b>$trapstr[$tttrap]</b></td>";
			$trap_list1 .= "<td>설치:$ttname<br>위력:$ttint</td>";
		}
	}
	if( $trap_list ne "" ){
		$trap_list = substr($trap_list,0,length($trap_list)-2);
	}



	if($def_num < $def_nums){
		$add .= "<option style=color:#000000;background-color:#FFDDDD; value=12>성의 요격(병력500명,훈련50 이상)";
	}

	open(IN,"./charalog/main/$xking.cgi");
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename) = split(/<>/,$E_DATA[0]);
	$king_name=$ename;
	open(IN,"./charalog/main/$x0.cgi");
	@S_DATA = <IN>;
	close(IN);
	($sid,$spass,$sname) = split(/<>/,$S_DATA[0]);
	$sub_name=$sname;

	$next_time = int(($kdate + $TIME_REMAKE - $tt) / 60);
	if($next_time < 0){
		$next_time = 0;
	}
	$del_out = $DEL_TURN - $ksub2;

	$dilect_mes = "";$m_hit=0;$i=1;$h=1;$j=1;$k=1;
	open(IN,"$MESSAGE_LIST") or &ERR('파일을 열지 않았습니다.');
	while (<IN>){
		my ($pid,$hid,$hpos,$hname,$hmessage,$pname,$htime,$hchara,$hcon,$hunit,$rank_mes) = split(/<>/);
		if($rank_mes eq "gg01" || $rank_mes eq "gg02"){$backpic = "background=$IMG/gunju.jpg";}else{$backpic="bgcolor=#000000";}
		if($MES_MAN < $i && $MES_ALL < $h && $MES_COU < $j && $MES_UNI < $k) { last; }
		if(111 eq "$pid" && $kpos eq $hpos){
			if($MES_ALL < $h ) { next; }
			$all_mes .= "<TR><TD width=100% $backpic><font size=2 color=#FFFFFF><b><img src=$IMG/$rank_mes\.jpg> <a href=\"javascript:info('$hid')\">$hname</a>($hid)\【$town_name[$hpos]】<BR>[<b>$hmessage</b>]<BR>$htime</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>\n";
			$h++;
		}elsif($kcon eq "$pid"){
			if($MES_COU < $j ) { next; }
			if($pid ne $hcon){
			$cou_mes .= "<TR><TD width=100% $backpic><font size=2 color=FFCC33><b><img src=$IMG/$rank_mes\.jpg> <a href=\"javascript:info('$hid')\">$hname</a>($hid)\【$town_name[$hpos]】</b></font><BR><font size=2 color=#FFFFFF>  「<b>$cou_name[$hcon]국 외교사자: $hmessage</b>」<br>$htime</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>";
			}else{
			$cou_mes .= "<TR><TD width=100% $backpic><font size=2 color=FFCC33><b><img src=$IMG/$rank_mes\.jpg> <a href=\"javascript:info('$hid')\">$hname</a>($hid)\【$town_name[$hpos]】</b></font><BR><font size=2 color=#FFFFFF>  「<b>$hmessage</b>」<br>$htime</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>";
			}
			$j++;
		}elsif($kid eq "$pid"){
			if($MES_MAN < $i ) { next; }
			$add_mes = "<b><font color=orange><a href=\"javascript:info('$hid')\">$hname</a>($hid)\【$town_name[$hpos]】</font> →<a href=\"javascript:info('$pid')\">$pname</a></b><BR>";
			$man_mes .= "<TR><TD width=100% $backpic><font size=2 color=#FFFFFF>$add_mes「<b>$hmessage</b>」</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>\n";
			$dilect_mes .= "<option value=\"$hid\"><a href=\"javascript:info('$kid')\">$hname</a>";
			$i++;
		}elsif(333 eq "$pid" && "$hunit" eq "$unit_id" && "$hcon" eq "$kcon" && "$xcid" ne "0"){
			if($MES_UNI < $k ) { next; }
			$unit_mes .= "<TR><TD width=100% $backpic><font size=2 color=orange><b><img src=$IMG/$rank_mes\.jpg> <a href=\"javascript:info('$hid')\">$hname</a>($hid) →<a href=\"javascript:info('$pid')\">$pname</a></b></font><BR><font size=2 color=#FFFFFF>  「<b>$hmessage</b>」</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>";
			$k++;
		}elsif($kid eq "$hid"){
			if($MES_MAN < $i ) { next; }
			$man_mes .= "<TR><TD width=100% $backpic><font size=2 color=skyblue><b><a href=\"javascript:info('$kid')\">$kname</a>($kid) →<a href=\"javascript:info('$pid')\">$pname</a></b></font><BR><font size=2 color=#FFFFFF>  「<b>$hmessage</b>」</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$kname\"></TD></TR>";
			$i++;
		}
	}
	close(IN);

	$m_hit=0;$i=1;$h=1;$j=1;$k=1;
	open(IN,"$MESSAGE_LIST2") or &ERR('파일을 열지 않았습니다.');
	while (<IN>){
		my ($pid,$hid,$hpos,$hname,$hmessage,$pname,$htime,$hchara,$hcon) = split(/<>/);
		if($MES_MAN < $i) { last; }
		if($kid eq "$pid"){
			$add_mes="";
			$add_sel="";
			$add_form1="";
			$add_form2="";
			if($htime eq "9999"){
			$add_mes = "<B><font color=skyblue>$hname님은 $cou_name[$hcon]국으로 망명하기를 권유하고 있습니다.</font><BR></B>";
			$add_sel = "<BR><input type=radio name=sel value=1>승낙한다<input type=radio name=sel value=0>거절한다<input type=submit value=\"대답\">";
			$add_form1="<form action=\"./mydata.cgi\" method=\"post\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=hcon value=$hcon><input type=hidden name=hid value=$hid><input type=hidden name=hpos value=$hpos><input type=hidden name=mode value=COU_CHANGE>";
			$add_form2="</form>";
			}else{
			$add_mes = "<B><font color=skyblue>$hname($hid) →$pname($pid)</font><BR></B>";
			}
			$man_mes2 .= "$add_form1<TR><TD width=100% bgcolor=#000000><font size=2 color=#FFFFFF>$add_mes「<b>$hmessage</b>」$add_sel</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>$add_form2\n";
			$dilect_mes .= "<option value=\"$hid\">$hname";
			$i++;
		}elsif($kid eq "$hid"){
			$man_mes2 .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=skyblue><b><a href=\"javascript:info('$kid')\">$kname</a>($hid) →<a href=\"javascript:info('$pid')\">$pname</a>($pid)</b></font><BR><font size=2 color=#FFFFFF>  「<b>$hmessage</b>」</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$kname\"></TD></TR>";
			$i++;
		}
	}
	close(IN);

	$zshiro2=$zshiro/10; $zdef_att2=$zdef_att/10; $znou2=$znou/10; $zsyo2=$zsyo/10;
	$zsub12=$zsub1/12;

	if($town_get[$kcon] eq 53){
	$haha = "<img src=$IMG/endding.gif><br><br>";
	}

	if($xch){
		$couch = "<a href=http://barosl.com/webirc/$xch?iframe=1&width=700&height=600 target=_blank><img src=$IMG/come8.jpg border=0></a>";
	}

	if($xking eq $kid || $x0 eq $kid || $x1 eq $kid || $x2 eq $kid || $x3 eq $kid || $x4 eq $kid || $x17 eq $kid || $x18 eq $kid || $x19 eq $kid || $x20 eq $kid){
		$king_com = "<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM><input type=image src=\"$IMG/come7.jpg\">";
	}

	if($cou_name[$kcon] ne ""){
		$come1 ="<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=COUNTRY_TALK><input type=image ALT='$cou_name[$kcon]국의 국가회의실입니다.' src=$IMG/come1.jpg>";
		$come2 = "<input type=hidden name=pass value=$kpass><input type=hidden name=mode value=LOCAL_RULE><input type=image ALT='$cou_name[$kcon]국의 국법일람입니다.' src=$IMG/come2.jpg>";
		$come4 = "<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=UNIT_SELECT><input type=image ALT='$cou_name[$kcon]국의 국가부대망입니다.' src=$IMG/come4.jpg>";
		$come6 = "<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=image src=$IMG/come6.jpg>";
	}else{
		$come1 ="<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=COUNTRY_TALK2><input type=image src=$IMG/come0.jpg>";
	}

	if($xking eq $kid || $x0 eq $kid || $x1 eq $kid || $x17 eq $kid){
		$hiyo = "<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=image src=\"$IMG/come9.jpg\">";
	}

	if($xking eq $kid || $x0 eq $kid || $x1 eq $kid || $x2 eq $kid || $x3 eq $kid || $x4 eq $kid || $x17 eq $kid || $x18 eq $kid || $x19 eq $kid || $x20 eq $kid){
		foreach(@COU_DATA){
			($xvcid,$xvname)=split(/<>/);
			$dilect_mes .= "<option value=\"$xvcid\">$xvname국";
		}
	}

	if($xmark < $BATTLE_STOP){
		$xc = $BATTLE_STOP - $xmark;
		$xaddmes = "<BR>전쟁금지턴은 앞으로 <font color=red>$xc</font>턴 남았습니다.";
	}

	$klank = int($kclass / $LANK);
	if($klank > 50){
		$klank=50;
	}
	&HEADER;


print <<"EOM";
<script language="javascript">

function balloonHint(Id)
{
balloonHint.layerId = Id;

document.addEventListener('mouseover', balloonHint.Show, false);
document.addEventListener('mouseout', balloonHint.Hide, false);
}
balloonHint.layerId = null;
balloonHint.Show = function (evt) {
if (typeof evt == "undefined" || typeof evt.target == "undefined") {
(evt=event).target = event.srcElement;
}

var hint = evt.target.getAttribute("hint");
if (hint == null || hint.length == 0) return;
if (balloonHint.layer == null) balloonHint.makeLayer();

with (balloonHint.layer) {
innerHTML = sourceHTML.replace("{{hint}}", hint);
show(evt.clientX, evt.clientY);
}
}

balloonHint.Hide = function (evt) {
if (typeof evt == "undefined" || typeof evt.target == "undefined") {
(evt=event).target = event.srcElement;
}

var hint = evt.target.getAttribute("hint");
if (hint == null || hint.length == 0) return;

balloonHint.layer.hide();
}

balloonHint.makeLayer = function()
{
if (typeof document.body == "undefined") {
document.body = document.getElementsByTagName("BODY")[0];
}

balloonHint.layer = document.getElementById(balloonHint.layerId);
balloonHint.layer.sourceHTML = balloonHint.layer.innerHTML;
balloonHint.layer.style.position = "absolute";

if (typeof window.createPopup == "undefined") {
balloonHint.layer.show = function(x, y) {
balloonHint.layer.style.display = "block";
balloonHint.layer.style.left = (x+document.body.scrollLeft+1) + "px";
balloonHint.layer.style.top =  (y+document.body.scrollTop+1) + "px";
}
balloonHint.layer.hide = function() {
balloonHint.layer.style.display = "none";
}
} else {
balloonHint.layer.popup = window.createPopup();
balloonHint.layer.show = function(x, y) {
with (balloonHint.layer) {
style.display = "block";
var w = offsetWidth, h = offsetHeight;
style.display = "none";
popup.document.body.innerHTML = innerHTML;
popup.show(x, y, w, h, document.body);
}
}
balloonHint.layer.hide = function() {
balloonHint.layer.popup.hide();
}
}
}

if (typeof document.addEventListener == "undefined") {
if (typeof document.attachEvent != "undefined") {
document.addEventListener = function (eventType, listener) {
document.attachEvent("on"+eventType, listener);
}
document.removeEventListener = function (eventType, listener) {
document.detachEvent("on"+eventType, listener);
}
}
}
</script>

<body bgcolor="white" text="black" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" background="$IMG/back.jpg">
<div id="balloonHint" style="display:none" width: 500px; height: 500px;">
<table cellpadding="0" cellspacing="0" width="200" height="100">
    <tr>
        <td width="1101" background="$IMG/sung0.jpg">
            {{hint}}
        </td>
    </tr>
</table>
</div>
<script language="javascript">balloonHint("balloonHint")</script>
<table align="center" cellpadding="0" cellspacing="0">
    <tr>
        <td width="950">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
         <td width="950" height="59" background="$IMG/backg.gif">
            <p>
	    <TABLE border=0 width=100% height=100%><TR><TD>
<TABLE border=0 width=100%>
<TR><TD colspan=2>

<table cellpadding="0" cellspacing="0" width="100%" align="center">
    <tr>
        <td width="10">
            <p><img src="$IMG/u1.jpg" border="0"></p>
        </td>
        <td background="$IMG/u2.jpg">
<font color=FFFFFF size=2><b>$xname국 지령 : $xmes</b></font>        </td>
        <td width="5">
            <p><img src="$IMG/u3.jpg" border="0"></p>
        </td>
    </tr>
</table>
</TD></TR><TR><TD width=50%>
<TABLE width=100% align="center"><TR><TD width=50%>
<br>
      <TABLE bgcolor=$bg_c width=100% height=5 border="0" cellspacing=0>
        <TBODY>
<TR><TH colspan= 13 bgcolor=442200><font color=FFFFFF>$new_date</TH></TR>

          <TR>
            <TD width=20 bgcolor=$TD_C2>-</TD>


EOM
&JIDO0;
print <<"EOM";
        </TBODY>
      </TABLE>
</TD></TR>
<TR><TD>
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>

<table align="center" cellpadding="0" cellspacing="0" width="526" height="207" background="$IMG/$zname1.jpg">
    <tr>
        <td width="1101">
            <table cellpadding="0" cellspacing="0" width="527" height="207" background="$IMG/$zname1.jpg">
                <tr>
                    <td width="309" height="142">
                  </td>
                    <td width="120" height="40" valign="up">
			$event_select
                    </td>
                    <td width="98">
                        <table cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="81" height="20">
                                </td>
                            </tr>
                            <tr>
                                <td width="81" height="19">
                                    <p><span style="font-size:9pt;"><font color="white">$znou/$znou_max</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="81" height="19">
                                    <p><span style="font-size:9pt;"><font color="white">$zsyo/$zsyo_max</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="81" height="19">
                                    <p><span style="font-size:9pt;"><font color="white">$zsub1/1200</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="81" height="19">
                                    <p><span style="font-size:9pt;"><font color="white">$zpri</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="81" height="19">
                                    <p><span style="font-size:9pt;"><font color="white">$zshiro/$zshiro_max</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="81" height="19">
                                    <p><span style="font-size:9pt;"><font color="white">$zdef_att/1000</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="81" height="8">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="309" height="60">
<table cellpadding="0" cellspacing="0" align="right">
    <tr>
<form action=\"./quest0.cgi\" method=\"post\">
        <td>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=QUEST><input type=image src=\"$IMG/jujem.gif\">
        </td>
</form>
<form action=\"./mydata.cgi\" method=\"post\">
        <td>
           $bongt
        </td>
</form>
<form action=\"./bong3.cgi\" method=\"post\">
        <td>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=BONG3><input type=image ALT='$zname성의 봉토일람입니다.' src=\"$IMG/bongto.jpg\">
        </td>
</form>
    </tr>
</table>
                  </td>
                    <td width="218" colspan="2">
            <table cellpadding="0" cellspacing="0" width="209">
                <tr>
                    <td width="209" height="2" colspan="4">
                       
                    </td>
                </tr>
                <tr>
                    <td width="58" height="16">
                    </td>
                    <td width="50" height="16">
                        <p align="center"><font color="white" face="돋움"><span style="font-size:9pt;">$cou_name[$zcon]</span></font></p>
                    </td>
                    <td width="46" height="16">
                    </td>
                    <td width="55" height="16">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$town_get[$zcon]도시</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="58" height="20">
                    </td>
                    <td width="50" height="20">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$king_name</span></font></p>
                    </td>
                    <td width="46" height="20">
                    </td>
                    <td width="55" height="20">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$zsyo_sal</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="58">
                    </td>
                    <td width="50">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$znum</span></font></p>
                    </td>
                    <td width="46">
                    </td>
                    <td width="55">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$znou_sal</span></font></p>
                    </td>
                </tr>
            </table>                    
</td>
                </tr>
            </table>
        </td>
    </tr>
</table>

<script>
function submit2(frm){
test=window.open('','tst',"width=60,height=80,scrollbars=1,menubar=0,toolbar=0,status=0,location=0,directories=0");
frm.submit();
}
</script>
<table cellpadding="0" cellspacing="0" width="526">
    <tr>
        <td width="25" height="113"><p><img src="$IMG/cb1.jpg" width="25" height="113" border="0"></p>
        </td>
        <td width="477" height="113" background="$IMG/cb.jpg">
            <table cellpadding="0" cellspacing="0" width="100%">
                <tr>
                    <td width="480" height="89">
                        <div align="left">
                            <table cellpadding="0" cellspacing="0">
                                <tr>
				<form action="./mydata.cgi" method="post" style="margin:0;padding:0;">
                                    <td>
					$come1
                                    </td></form>
				    <form action="./mydata.cgi" method="post" style="margin:0;padding:0;">
                                    <td>
                                    <input type=hidden name=id value=$kid>
					$come2
                                    </td></form>
				    <form action="./mydata.cgi" method="post">
                                    <td>
                                       <input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=LETTER><input type=image src="$IMG/come3.jpg">
                                    </td></form>
				    <form action="./mydata.cgi" method="post">
                                    <td>
				$come4
                                    </td></form>
				    <form action="./mylog.cgi" method="post">
                                    <td>
                                    <input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=image src="$IMG/come5.jpg">
                                    </td></form>
				    <form action="./mycou.cgi" method="post">
                                    <td>
$come6
                                    </td></form>
                                    <td>
					$couch
                                    </td>
				    <form action="./mydata.cgi" method="post" style="margin:0;padding:0;">
                                    <td>
                                    $king_com
                                    </td>
</form>
				    <form action="./mylog1.cgi" method="post">
                                    <td>
                                       $hiyo
                                    </td></form>
				 	<form action="./setting.cgi" method="post">
                                    <td>     
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=image src="$IMG/come11.jpg">
                                    </td>
				    </form>
				    <form action="$FILE_STATUS" method="post">
                                    <td>     
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=image src="$IMG/come10.jpg">
                                    </td>
				    </form>
                                </tr>
                            </table>
                        </div>
                    </td>
                </tr>
                <tr>
                    <td width="480" height="23">
                    </td>
                </tr>
            </table>
        </td>
        <td width="24" height="113">
            <p><img src="$IMG/cb2.jpg" width="25" height="113" border="0"></p>
        </td>
    </tr>
</table>
<div style="width:526px;margin:6px auto 10px auto;display:flex;gap:8px;justify-content:flex-end;align-items:center">
<a class="btn" href="./plan.cgi?id=$kid&pass=$kpass&mode=PLAN">30TURN PLAN</a>
</div>
<form action="./command.cgi" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<table cellpadding="0" cellspacing="0" width="526" height="150" background="$IMG/cc.jpg">
    <tr>
        <td width="1101" background="$IMG/cc.jpg">
            <table cellpadding="0" cellspacing="0" width="100%">
                <tr>
                    <td width="526" height="30" colspan="2">
                    </td>
                </tr>
                <tr>
                    <td width="115" height="96" rowspan="2">                        <p align="center"><select name=no size="6" MULTIPLE style="color:rgb(204,204,0); background-color:rgb(93,40,0);">
<option value="all">전체선택
EOM
	for($i=0;$i<$MAX_COM;$i++){
		$no = $i+1;
		if($i eq "0"){
		print "<option value=\"$i\" SELECTED>$no턴";
		}else{
		print "<option value=\"$i\">$no턴";
		}
	}

print <<"EOM";
</select></td>
                    <td width="411" height="32" valign="bottom">
<select name=mode size="1">
<option value="0" color:0099ff;>아무것도 하지 않는다.
<option style="color:#000000;background-color:#C7FFC9;" value="">===================== 내정 =====================
<option style="color:#000000;background-color:#C7FFC9;" value="1">농업개발(지력영향 금50)  $eventon
<option style="color:#000000;background-color:#C7FFC9;" value="2">상업발전(지력영향 금50)
<option style="color:#000000;background-color:#C7FFC9;" value="29">기술개발(지력영향 금50)
<option style="color:#000000;background-color:#C7FFC9;" value="3">수비대양성(무력영향 금50)
<option style="color:#000000;background-color:#C7FFC9;" value="30">방어시설구축(통솔영향 금50)
<option style="color:#000000;background-color:#C7FFC9;" value="8">쌀을 베푼다(매력영향 쌀100)
<option style="color:#000000;background-color:#FFDDDD;" value="">===================== 군사 =====================
<option style="color:#000000;background-color:#FFDDDD;" value="9">징병하기(통솔영향)
<option style="color:#000000;background-color:#FFDDDD;" value="11">병사훈련(통솔영향)
<option style="color:#000000;background-color:#FFDDDD;" value="31">병사맹훈련(통솔영향 쌀500)
$add
<option style="color:#000000;background-color:#FFDDDD;" value="13">출병
<option style="color:#000000;background-color:#FFDDDD;" value="44">원군(통솔영향)
<option style="color:#000000;background-color:#FFDDDD;" value="68">주민이주(통솔영향)
$dok
<option style="color:#000000;background-color:#FFDDDD;" value="">===================== 함정 =====================
<option style="color:#000000;background-color:#FFDDDD;" value="52">허보(매력영향 금100)
<option style="color:#000000;background-color:#FFDDDD;" value="50">화계(지력영향 기술치500 금300)
<option style="color:#000000;background-color:#FFDDDD;" value="51">낙석(지력영향 기술치800 금500)
<option style="color:#000000;background-color:#FFDDDD;" value="">===================== 계략 =====================
<option style="color:#000000;background-color:#FFDDDD;" value="33">성벽파괴(지력영향 금100)
<option style="color:#000000;background-color:#FFDDDD;" value="37">도시방화(지력영향 금100)
<option style="color:#000000;background-color:#FFDDDD;" value="35">유언비어(매력영향 금100)
<option style="color:#000000;background-color:#DBDBFF;" value="">===================== 상인 =====================
<option style="color:#000000;background-color:#DBDBFF;" value="14">물품거래
<option style="color:#000000;background-color:#DBDBFF;" value="60">왕서방의 아이템상점
<option style=color:#000000;background-color:#DBDBFF; value=58>송금(수수료10%)
<option style="color:#000000;background-color:#CCCCCC;" value="">===================== 기타 =====================
<option style="color:#000000;background-color:#CCCCCC;" value="55">특기교육소
<option style="color:#000000;background-color:#CCCCCC;" value="62">일기토&설전 겨루기
<option style="color:#000000;background-color:#CCCCCC;" value="24">등용(매력영향)
<option style="color:#000000;background-color:#CCCCCC;" value="17">이동
<option style="color:#000000;background-color:#CCCCCC;" value="61">휴식
<option style="color:#000000;background-color:#CCCCCC;" value="65">숙박(휴식 2배효과, 금300)
$fdfd
$add_com
$add_com1
</select><input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BC[$xele]; border-width:1; border-color:black; border-style:solid;" value="실행"></form>
                    </td>
                </tr>
                <tr>
                    <td width="411" height="62">
                        <table cellpadding="0" cellspacing="0" width="392">
                        <tr>
                                <td width="392" height="20">
                                <p align="center"><span style="font-size:9pt;"><b>다음 턴까지 <font color=red>$next_time</font>분 남았습니다.</b></span>                                </td>
                        </tr>
                        <tr>
                                <td width="392" height="23">
                                <p align="center"><span style="font-size:9pt;"><b>삭제방치턴은 <font color=red>$del_out</font>턴 남았습니다.$xaddmes</b></span>                                </td>
                        </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br><br>
</TABLE>

</TD><TD>

<TABLE><TR><TD>
<TABLE width=100% bgcolor=$TABLE_C cellspacing=1><TBODY BGCOLOR=$TD_C2>
<TR><TH bgcolor=#000000 colspan=3><img src="$IMG/com.gif"></TH></TR>
$com_list
</TABLE>

</TD></TR>
<TR><TD>

<table cellpadding="0" cellspacing="0" width="355" height="244">
    <tr>
        <td width="1101" background="$IMG/st.jpg">
            <table cellpadding="0" cellspacing="0" width="355">
                <tr>
                    <td width="355" height="13" colspan="4">
                    </td>
                </tr>
                <tr>
                    <td width="21" height="221" rowspan="3">
                    </td>
                    <td width="64" height="87">
                        <p><img src="$IMG/$kchara.gif" border="0"></p>
                    </td>
                    <td width="16" height="221" rowspan="3">
                    </td>
                    <td width="254" height="221" rowspan="3">
                        <table cellpadding="0" cellspacing="0" width="244">
                            <tr>
                                <td width="90" height="24">
                                </td>
                                <td width="80" height="24">
$kstrt (Ex:$kstr_ex)                                 </td>
                                <td width="55" height="24">
                                </td>
                                <td width="86" height="24">
Lv.$klevel                               </td>
                            </tr>
                            <tr>
                                <td width="40" height="24">
                                </td>
                                <td width="80" height="24">
$kintt (Ex:$kint_ex)                                 </td>
                                <td width="40" height="24">
                                </td>
                                <td width="86" height="24">
$kexp / $levelup                                </td>
                            </tr>
                            <tr>
                                <td width="40" height="24">
                                </td>
                                <td width="80" height="24">
$kleat (Ex:$klea_ex)                                </td>
                                <td width="40" height="24">
                                </td>
                                <td width="86" height="24">
$kgold                                </td>
                            </tr>
                            <tr>
                                <td width="81" height="24">
                                </td>
                                <td width="80" height="24">
$kchat (Ex:$kcha_ex)                                </td>
                                <td width="40" height="24">
                                </td>
                                <td width="86" height="24">
$krice
                                </td>
                            </tr>
                            <tr>
                                <td width="244" colspan="4" height="7">
                                </td>
                            </tr>
                            <tr>
                                <td width="40" height="24">
                                </td>
                                <td width="80" height="24">
$cou_name[$kcon]국                                </td>
                                <td width="40" height="24">
                                </td>
                                <td width="86" height="24">
$SOL_TYPE[$ksub1_ex]                                </td>
                            </tr>
                            <tr>
                                <td width="40" height="24">
                                </td>
                                <td width="80" height="24">
$karmname</td>
                                <td width="40" height="24">
                                </td>
                                <td width="86" height="24">
$ksol명                                </td>
                            </tr>
                            <tr>
                                <td width="40" height="24">
                                </td>
                                <td width="80" height="24">
$kproname                               </td>
                                <td width="40" height="24">
                                </td>
                                <td width="86" height="24">
$kgat                                </td>
                            </tr>
                            <tr>
                                <td width="40" height="24">
                                </td>
                                <td width="357" height="27" colspan="3">
$uunit_name                                </td>
                            </tr>
                            <tr>
                                <td width="244" height="19" colspan="4">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td width="64" height="75">
                        $xname국<br>$rank_mes<br><b><a href=\"javascript:info('$kid');\">$kname</a></b><br>$sangtae<br>SP:$kpoint</td>
                </tr>
                <tr>
                    <td width="64" height="44">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
</TD></TR>
</TABLE>
</TD></TR>



<table cellpadding="0" cellspacing="0">
    <tr>
        <td width="920" height="19" colspan="2">
<TABLE width="100%" height="20" bgcolor=$TABLE_C align="center"><TR><TD bgcolor=$TD_C1 height="20">접속장수:$m_list</TD></TR></TABLE></td>
    </tr>
    <tr>
        <td width="920" height="5" colspan="2">
</td>
    </tr>
    <tr>
        <td width="420" height="157">
<table bgcolor=$TD_C1 border="1" align="center" width="418">
    <tr>
        <td bgcolor=$TD_C1 height="20" width="408">
            <center>$zname성의 벌판 [요격가능인원 : <b>$def_nums</b>명]</center> 
</td>
    </tr>
<tr>
<td width="408" height="60">
            <table border="1">
                <tr>
                 $trap_list

    </tr>
                <tr>
                 $trap_list1

    </tr>
</table>
</td>
</tr>
    <tr>
        <td width="408" height="140">


<table cellpadding="0" cellspacing="0" width="408" height="140">
    <tr>
        <td width="805" background="$IMG/$sungru.jpg">
            <div align="right">
            <table cellpadding="0" cellspacing="0" width="300">
                <tr>
                    <td height=8 colspan="5" width="300">
                    </td>
                </tr>
                <tr>
                    <td width="60" height="40">
                       $def_list1
                    </td>
                    <td width="60" height="40">
                    </td>
                    <td width="60" height="40">
                    </td>
                    <td width="60" height="40">
                       &nbsp;                    </td>
                    <td width="60" height="40">
                       $def_list4                    </td>
                </tr>
                <tr>
                    <td width="60" height="40">
                    </td>
                    <td width="60" height="40">
                       $def_list2
                    </td>
                    <td width="60" height="40">
                       
                    </td>
                    <td width="60" height="40">
                     
                       $def_list5                    </td>
                    <td width="60" height="40">

                    </td>
                </tr>
                <tr>
                    <td width="60" height="33">
                       $def_list3                    </td>
                    <td width="60" height="33">
                    </td>
                    <td width="60" height="33">
                       $def_list6                    </td>
                    <td width="60" height="33">
                    </td>
                    <td width="60" height="33">

                    </td>
                </tr>
            </table>
            </div>
        </td>
    </tr>
</table>


</td>
    </tr>
</table>
</td>
        <td height="157"><TABLE width=500 height=232 bgcolor=$TABLE_C><TR><TD bgcolor=$TD_C1>$S_MES</TD></TR></TABLE></td>
    </tr>
</table>

<TR><TD colspan=2>
<table width=98% cellpadding="0" cellspacing="0">
<tr>
<td colspan="2" width=100%>
<TABLE width="100%" bgcolor=$ELE_BG[$cou_ele[$kcon]]><TR><TD bgcolor=$ELE_C[$cou_ele[$kcon]]>$log_list</TD></TR>
</TABLE>
</td>
    </tr>
<tr>


<td width=43%>
<TABLE width="100%" bgcolor=$ELE_BG[$cou_ele[$kcon]]><TR><TD height="5"><img src="$IMG/log_left.gif"></TD></TR><TR><TD bgcolor=$ELE_C[$cou_ele[$kcon]] height="13">$log_list2</TD></TR></TABLE>
</td>
<td width=55%>
<TABLE width="100%" bgcolor=$ELE_BG[$cou_ele[$kcon]]><TR><form action="./battlelog.cgi" method="post"><TD height="5"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=image src="$IMG/log_right.gif"></TD></form></TR><TR><TD bgcolor=$ELE_C[$cou_ele[$kcon]] height="13">$log_list1</TD></TR></table>
</td>
</tr>
</table>

<form action="$FILE_MYDATA" method="post">
<center>커뮤니케이션 : <input type="text" name=message size=60>
  <select name=mes_id><option value="$xcid">[국가채널] $xname국<option value="111">[지역채널] $zname성<option value="333">[부대채널] $uunit_name부대$dilect_mes</select>
  <input type=hidden name=id value=$kid>
  <input type=hidden name=name value=$kname>
  <input type=hidden name=pass value=$kpass>
  <input type=hidden name=mode value=MES_SEND>
  <input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;" value="메시지입력"></form>
<TABLE width=100%><TBODY>
<TR><TD width=50%  valign="up">
	[지역채널] $zname성 ($MES_ALL건)
	<TABLE width=100% bgcolor=880000><TBODY>
	$all_mes
	</TBODY></TABLE>

	[개인채널] $kname님 ($MES_MAN건)
	<TABLE width=100% bgcolor=008800><TBODY>
	$man_mes
	</TBODY></TABLE>

	[밀서채널] $kname님 ($MES_MAN건)
	<TABLE width=100% bgcolor=008800><TBODY>
	$man_mes2
	</TBODY></TABLE>
</TD><TD valign="up">
	[국가채널] $xname국 ($MES_COU건)
	<TABLE width=100% bgcolor=000088><TBODY>
	$cou_mes
	</TBODY></TABLE>

	[부대채널] $uunit_name부대 ($MES_UNI건)
	<TABLE width=100% bgcolor=AA8833><TBODY>
	$unit_mes
	</TBODY></TABLE>

</TD></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD colspan=2>
</form>
<form action="$FILE_TOP" method="post">
<center><input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;" value="삼국지 모의전투 NET 로그아웃하기"></form>
</TD></TR>
</TABLE>
</TD></TR></TABLE>
	    </p>
        </td>
    </tr>
    <tr width="950" height="0" background="$IMG/backg.gif">
        <td background="$IMG/backg.gif">
            <p><center><img src="$IMG/down.gif" width="950" height="26" border="0"></p>
        </td>
    </tr>
</table>
</body>
EOM
	&FOOTER;
	exit;
}