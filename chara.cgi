#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

&DECODE;
&BODY;

sub BODY {



	if ($in{'id'} =~ /[^0-9a-zA-Z]/){
		&ERR2("에러입니다.");
	}

	&TOWN_DATA_OPEN("$kpos");




	open(IN,"./charalog/main/$in{'id'}.cgi") or &ERR2('ID와 패스가 올바르지 않습니다!');
	@CN_DATA = <IN>;
	close(IN);

	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct,$klevel,$kexp,$kcodea,$kcodeb,$kqpoint) = split(/<>/,$CN_DATA[0]);
	($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex) = split(/,/,$ksub1);
	
	$levelup = int(200 * (1+($klevel*0.1)));

	foreach(@TOWN_DATA){
		($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy,$zzsouba,$zzdef_att,$zzsub1,$zzsub2,$z[0],$z[1],$z[2],$z[3],$z[4],$z[5],$z[6],$z[7],$zzname1,$zzname2,$zzbong1,$zzbong2,$zzbong3)=split(/<>/);
		if($kid eq "$zzbong1" || $kid eq "$zzbong2" || $kid eq "$zzbong3"){
			$bongto = "$zzname";
		}
	}

	$bos = int($bo_ex/3);
	if($bo_ex < 3){$bos = 0;}
	$gis = int($gi_ex/3);
	if($gi_ex < 3){$gis = 0;}
	$chs = int($ch_ex/3);
	if($ch_ex < 3){$chs = 0;}
	$gus = int($gu_ex/3);
	if($gu_ex < 3){$gus = 0;}

	if($go_ex < 500){
		$sangtae = "<font color=301ED8>건강</font>";
	}elsif($go_ex <1000 && $go_ex > 499){
		$sangtae = "<font color=000000>보통</font>";
	}elsif($go_ex < 1250 && $go_ex > 999){
		$sangtae = "<font color=730C86>나태</font>";
	}elsif($go_ex < 1500 && $go_ex > 1249){
		$sangtae = "<font color=C51B4B>중태</font>";
	}elsif($go_ex <1700 && $go_ex > 1499){
		$sangtae = "<font color=FF0000>위험</font>";
	}

	if($kskill =~ /Aa/){
		$skill_list .= "《농업》";
	}
	if($kskill =~ /Ab/){
		$skill_list .= "《거래》";
	}
	if($kskill =~ /Ac/){
		$skill_list .= "《덕망》";
	}
	if($kskill =~ /Ba/){
		$skill_list .= "《상업》";
	}
	if($kskill =~ /Bb/){
		$skill_list .= "《수완》";
	}
	if($kskill =~ /Bc/){
		$skill_list .= "《고용》";
	}
	if($kskill =~ /Ca/){
		$skill_list .= "《기술》";
	}
	if($kskill =~ /Cb/){
		$skill_list .= "《회피》";
	}
	if($kskill =~ /Cc/){
		$skill_list .= "《연구》";
	}
	if($kskill =~ /Da/){
		$skill_list .= "《양성》";
	}
	if($kskill =~ /Db/){
		$skill_list .= "《모병》";
	}
	if($kskill =~ /Dc/){
		$skill_list .= "《설치》";
	}
	if($kskill =~ /Ea/){
		$skill_list .= "《훈련》";
	}
	if($kskill =~ /Eb/){
		$skill_list .= "《독려》";
	}
	if($kskill =~ /Ec/){
		$skill_list .= "《원전》";
	}
	if($kskill =~ /Fa/){
		$skill_list .= "《민심》";
	}
	if($kskill =~ /Fb/){
		$skill_list .= "《매료》";
	}
	if($kskill =~ /Fc/){
		$skill_list .= "《매전》";
	}
	if($kskill =~ /Ga/){
		$skill_list .= "《고양》";
	}
	if($kskill =~ /Gb/){
		$skill_list .= "《병략》";
	}
	if($kskill =~ /Gc/){
		$skill_list .= "《일섬》";
	}




	&COUNTRY_DATA_OPEN("$kcon");
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




	&CHARA_ITEM_OPEN;

	$kstrplus = $itemstr[$karm] + $itemstr[$kbook];
	$kintplus = $itemint[$karm] + $itemint[$kbook];
	$kleaplus = $itemlea[$karm] + $itemlea[$kbook];
	$kchaplus = $itemcha[$karm] + $itemcha[$kbook];
	$kstrtotal = $kstrt;
	$kinttotal = $kintt;
	$kleatotal = $kleat;
	$kchatotal = $kchat;

	if( $karm > 0 ){
		$item_list .= $itemname[$karm] . ", ";
	}
	if( $kbook > 0 ){
		$item_list .= $itemname[$kbook] . ", ";
	}
	if( $item_list ne "" ){
		$item_list = substr($item_list,0,length($item_list)-2);
	}

	if( $kstrtotal > 100 ){
		$len_kstr = 100;
		$over = $kstrtotal-100;
	}else{
		$len_kstr = $kstrtotal;
		$len_kstr2 = '<img src="$img/bar2.gif" width="'.(100 - $len_kstr).'" height="5">';
	}
	if( $kinttotal > 100 ){
		$len_kint = 100;
		$over = $kinttotal-100;
	}else{
		$len_kint = $kinttotal;
		$len_kint2 = '<img src="$img/bar2.gif" width="'.(100 - $len_kint).'" height="5">';
	}
	if( $kleatotal > 100 ){
		$len_klea = 100;
		$over = $kleatotal-100;
	}else{
		$len_klea = $kleatotal;
		$len_klea2 = '<img src="$img/bar2.gif" width="'.(100 - $len_klea).'" height="5">';
	}
	if( $kchatotal > 100 ){
		$len_kcha = 100;
		$over = $kchatotal-100;
	}else{
		$len_kcha = $kchatotal;
		$len_kcha2 = '<img src="$img/bar2.gif" width="'.(100 - $len_kcha).'" height="5">';
	}
	if($go_ex>1700 ){
		$len_go = int(1700/17);
		$over = int($go_ex-1700/17);
	}else{
		$len_go = int($go_ex/17);
		$len_go2 = '<img src="$img/bar2.gif" width="'.(100 - $len_go).'" height="5">';
	}

	if( $kstrplus > 0 ){
		$kstrplusmes = "(+$kstrplus)";
	}
	if( $kintplus > 0 ){
		$kintplusmes = "(+$kintplus)";
	}
	if( $kleaplus > 0 ){
		$kleaplusmes = "(+$kleaplus)";
	}
	if( $kchaplus > 0 ){
		$kchaplusmes = "(+$kchaplus)";
	}
	if( $bo_ex > 0 ){
		$bomes = "(+$kchaplus)";
	}


	if( $kcon != 0 ){
		$con_name = "$cou_name[$kcon]국";
	}else{
		$con_name = "무소속";
	}

	open(IN,"./charalog/history/$in{'id'}.cgi") or &ERR("지정된 파일이 열리지 않습니다.");
	@HISTORY_DATA = <IN>;
	close(IN);

	print "Cache-Control: no-cache\n";
	print "Pragma: no-cache\n";
	print "Content-type: text/html\n\n";

print <<"EOM";
<html>
<head>
<META HTTP-EQUIV="Content-type" CONTENT="text/html; charset=euc-kr">
<title>칠랑서버 $kname 열전</title>
<STYLE type="text/css">
<!--
BODY,TR,TD,TH{
font-size:9pt;
line-height: 10pt;
}
.text { font-size: 9pt; line-height: 14pt; }
.8pttext { font-size: 8pt; line-height: 14pt; }
-->
</STYLE>
</head>
<body bgcolor="#F0E8E0" text="" link="#993300" vlink="#993300" alink="#993300" topmargin="0" leftmargin="0" marginwidth="0" marginheight="0" onload="window.focus()">
	<TABLE width="100%" bgcolor=$ELE_BG[$cou_ele[$kcon]] cellpadding="2" cellspacing="1" align="center">
	<TR><TH colspan=7 bgcolor=$ELE_BG[$cou_ele[$kcon]]><font color=$ELE_C[$cou_ele[$kcon]]>$rank_mes $kname</font></TH></TR>

	<TR bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<TD width=64 rowspan="5">
		<img src=$IMG/$kchara.gif>
	</TD>
	<TD width=40>소속</TD>
	<TD width=120>$con_name</TD>
	</TR>
	<TR bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<TD>연령</TD>
	<TD>$kbank</TD>
	</TR>
	<TR bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<TD>레벨</TD>
	<TD>$klevel ($kexp / $levelup)<br>총경험치:$kclass<br>공헌치:$kcex</TD>
	</TR>
	<TR bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<TD>고향</TD>
	<TD>$town_name[$kct]</TD>
	</TR>
	<TR bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<TD>봉토</TD>
	<TD>$bongto</TD>
	</TR>
	<TR>
	<TD colspan="3" bgcolor=$ELE_C[$cou_ele[$kcon]]>

		<TABLE WIDTH="100%">
		<TR>
		<TD>무력</TD>
		<TD align="right"><b>$kstrtotal</b></TD>
		<TD align="left"><b>$kstrplusmes</b></TD>
		<TD><img src="$IMG/bar.gif" width="$len_kstr" height="8">$len_kstr2</TD>
		</TR>
		<TR>
		<TD>지력</TD>
		<TD align="right"><b>$kinttotal</b></TD>
		<TD align="left"><b>$kintplusmes</b></TD>
		<TD><img src="$IMG/bar.gif" width="$len_kint" height="8">$len_kint2</TD>
		</TR>
		<TR>
		<TD>통솔력</TD>
		<TD align="right"><b>$kleatotal</b></TD>
		<TD align="left"><b>$kleaplusmes</b></TD>
		<TD><img src="$IMG/bar.gif" width="$len_klea" height="8">$len_klea2</TD>
		</TR>
		<TR>
		<TD>매력</TD>
		<TD align="right"><b>$kchatotal</b></TD>
		<TD align="left"><b>$kchaplusmes</b></TD>
		<TD><img src="$IMG/bar.gif" width="$len_kcha" height="8">$len_kcha2</TD>
		</TR>

		</TABLE>

	</TD>
	</TR>
	<TR>
	<TD colspan="3" bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<TABLE WIDTH="100%">
	<TD width=40>피로도</TD>
	<TD width=44 align="right"><b>$sangtae</b></TD>
	<TD width=100>
            <table cellpadding="0" cellspacing="0" WIDTH="100%" background="$IMG/bar3.gif">
                <tr>
                    <td>
		<img src="$IMG/bar2.gif" width="$len_go" height="8">$len_go2</TD>
                    </td>
                </tr>
            </table>
	<td></td>
	</TR>
	</TABLE>
	</td>
	</tr>
	<tr>
	<td colspan="3" width=100%>
<table width=100% bgcolor=$ELE_C[$cou_ele[$kcon]]>
    <tr>
        <td colspan="4" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
            <p align="center"><font color=$ELE_C[$cou_ele[$kcon]]><b>병과숙련</b></font></p>
        </td>
    </tr>
    <tr>
        <td width="25%" height="7" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
            <p align="center"><font color=$ELE_C[$cou_ele[$kcon]]>보병계열</font></p>
        </td>
        <td width="25%" height="7" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
            <p align="center"><font color=$ELE_C[$cou_ele[$kcon]]>기병계열</font></p>
        </td>
        <td width="25%" height="7" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
            <p align="center"><font color=$ELE_C[$cou_ele[$kcon]]>창병계열</font></p>
        </td>
        <td width="25%" height="7" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
            <p align="center"><font color=$ELE_C[$cou_ele[$kcon]]>귀병계열</font></p>
        </td>
    </tr>
    <tr>
        <td>
            <p align="center">Lv.$bos</p>
        </td>
        <td>
            <p align="center">Lv.$gis</p>
        </td>
        <td>
            <p align="center">Lv.$chs</p>
        </td>
        <td>
            <p align="center">Lv.$gus</p>
        </td>
    </tr>
</table>
	</td>
	</tr>
	</TABLE>
EOM
	if( $kskill ne "" ){
print <<"EOM";
	<TABLE width="100%" bgcolor=$ELE_BG[$cou_ele[$kcon]] cellpadding="2" cellspacing="1" align="center">
	<TR><TH colspan=7 bgcolor=$ELE_BG[$cou_ele[$kcon]]><font color=$ELE_C[$cou_ele[$kcon]]>소유특기</font></TH></TR>
	<TR>
	<TD bgcolor=$ELE_C[$cou_ele[$kcon]] class="text">$skill_list</TD>
	</TR>
	</TABLE>
EOM

	}

	open(IN,"$QUEST_DATA");
	@QUEST_DATA = <IN>;
	close(IN);

	foreach(@QUEST_DATA){
		($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal) = split(/<>/);
		if($kcodea =~ /$qcode/){
		$quest_list = "<b>[ $quest ]</b><br>$qseal : $kqpoint/$qlimit";
		}
	}
	if( $kcodea ne "" ){
print <<"EOM";
	<TABLE width="100%" bgcolor=$ELE_BG[$cou_ele[$kcon]] cellpadding="2" cellspacing="1" align="center">
	<TR><TH colspan=7 bgcolor=$ELE_BG[$cou_ele[$kcon]]><font color=$ELE_C[$cou_ele[$kcon]]>수행중인 퀘스트</font></TH></TR>
	<TR>
	<TD bgcolor=$ELE_C[$cou_ele[$kcon]] class="text">$quest_list</TD>
	</TR>
	</TABLE>
EOM
	}
	if( $kmes ne "" ){
print <<"EOM";
	<TABLE width="100%" cellpadding="2" cellspacing="1" align="center">
	<TR><TH colspan=7 bgcolor=$ELE_BG[$cou_ele[$kcon]]><font color=$ELE_C[$cou_ele[$kcon]]>자기소개</font></TH></TR>
	<TR>
	<TD bgcolor=$ELE_C[$cou_ele[$kcon]] class="text">$kmes</TD>
	</TR>
	</TABLE>
EOM
	}
print <<"EOM";
	<TABLE width="100%" bgcolor=$ELE_BG[$cou_ele[$kcon]] cellpadding="2" cellspacing="1" align="center">
	<TR><TH colspan=7 bgcolor=$ELE_BG[$cou_ele[$kcon]]><font color=$ELE_C[$cou_ele[$kcon]]>$kname 열전</font></TH></TR>
	<TR>
	<TD bgcolor=$ELE_C[$cou_ele[$kcon]] class="text">
EOM
	foreach(@HISTORY_DATA){
		($date,$value) = split(/: /,$_);
		print "<span class=8pttext>".$date.":</span>".$value."<br>";
	}
print <<"EOM";
	</TD>
	</TR>
	</TABLE>
</body>
</html>
EOM

}
