sub GET_SOL {

	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않았습니다.");}
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TOWN_DATA_OPEN($kpos);
	&TIME_DATA;
	&COUNTRY_DATA_OPEN("$kcon");

	# --- v20 UI: show troop region locks (added; no deletions) ---
	my ($__tx,$__ty)=(-1,-1);
	my $__pos_idx = $kpos;
	if($__pos_idx ne "" && $__pos_idx =~ /^\d+$/){
		open(__TIN,"$F_TOWN_LIST");
		my @__TD=<__TIN>;
		close(__TIN);
		if($__pos_idx <= $#__TD){
			my @__F=split(/<>/, $__TD[$__pos_idx]);
			$__tx=$__F[10]; $__ty=$__F[11];
		}
	}
	my $__region="";
	if($__tx ne "" && $__ty ne "" && $__tx >= 0 && $__ty >= 0){
		if($__tx >= 9){ $__region="korea"; }
		elsif($__ty >= 8 && $__tx <= 4){ $__region="nanman"; }
		elsif($__tx >= 7 && $__ty <= 3){ $__region="liaodong"; }
		else{ $__region="central"; }
	}
	my %__LOCK=();
	if($__region ne ""){
		$__LOCK{11}=($__region ne "korea");
		$__LOCK{8}=($__region ne "nanman");
		$__LOCK{5}=($__region ne "liaodong");
		$__LOCK{12}=($__region ne "central");
		$__LOCK{17}=($__region ne "central");
	}
	my $BUYBTN5  = ($__LOCK{5}  ? '<input type=button value=LOCKED disabled>' : '<input type=submit value=HIRE>');
	my $BUYBTN8  = ($__LOCK{8}  ? '<input type=button value=LOCKED disabled>' : '<input type=submit value=HIRE>');
	my $BUYBTN11 = ($__LOCK{11} ? '<input type=button value=LOCKED disabled>' : '<input type=submit value=HIRE>');
	my $BUYBTN12 = ($__LOCK{12} ? '<input type=button value=LOCKED disabled>' : '<input type=submit value=HIRE>');
	my $BUYBTN17 = ($__LOCK{17} ? '<input type=button value=LOCKED disabled>' : '<input type=submit value=HIRE>');
	my $LOCK_NOTE = '';
	if($__region ne ''){
		$LOCK_NOTE = '<div style="width:438px;margin:6px auto;padding:6px;border:1px solid #999;background:#f5f5f5;color:#000;font-size:9pt;">REGION: '.uc($__region).' / LOCKED troops show as LOCKED</div>';
	}

	&HEADER;
	$no = $in{'no'} + 1;

	$get_sol = ($kleat*30) - $ksol;

	foreach(@TOWN_DATA){
	($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy)=split(/<>/);
	if("$zzx" eq "$j" && "$zzy" eq "$i"){$m_hit=1;last;}
	$zx++;
				}


	if($kskill =~ /Fc/){
		$max0 = $SOL_PRICE[0] * 2;
		$max1 = $SOL_PRICE[1] * 2;
		$max2 = $SOL_PRICE[2] * 2;
		$max3 = $SOL_PRICE[3] * 2;
		$max4 = $SOL_PRICE[4] * 2;
		$max5 = $SOL_PRICE[5] * 2;
		$max6 = $SOL_PRICE[6] * 2;
		$max7 = $SOL_PRICE[7] * 2;
		$max8 = $SOL_PRICE[8] * 2;
		$max9 = $SOL_PRICE[9] * 2;
		$max10 = $SOL_PRICE[10] * 2;
		$max11 = $SOL_PRICE[11] * 2;
		$max12 = $SOL_PRICE[12] * 2;
		$max13 = $SOL_PRICE[13] * 2;
		$max14 = $SOL_PRICE[14] * 2;
		$max15 = $SOL_PRICE[15] * 2;
		$max16 = $SOL_PRICE[16] * 2;
		$max17 = $SOL_PRICE[17] * 2;
		$max18 = $SOL_PRICE[18] * 2;
		$max19 = $SOL_PRICE[19] * 2;
		$max20 = $SOL_PRICE[20] * 2;
	}else{
		$max0 = $SOL_PRICE[0];
		$max1 = $SOL_PRICE[1];
		$max2 = $SOL_PRICE[2];
		$max3 = $SOL_PRICE[3];
		$max4 = $SOL_PRICE[4];
		$max5 = $SOL_PRICE[5];
		$max6 = $SOL_PRICE[6];
		$max7 = $SOL_PRICE[7];
		$max8 = $SOL_PRICE[8];
		$max9 = $SOL_PRICE[9];
		$max10 = $SOL_PRICE[10];
		$max11 = $SOL_PRICE[11];
		$max12 = $SOL_PRICE[12];
		$max13 = $SOL_PRICE[13];
		$max14 = $SOL_PRICE[14];
		$max15 = $SOL_PRICE[15];
		$max16 = $SOL_PRICE[16];
		$max17 = $SOL_PRICE[17];
		$max18 = $SOL_PRICE[18];
		$max19 = $SOL_PRICE[19];
		$max20 = $SOL_PRICE[20];
	}

	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

		if($zsub1 > 100){
		$by1 = "FFFFFF"}else{$by1 = "FF0000"}
		if($zsub1 > 250){
		$by2 = "FFFFFF"}else{$by2 = "FF0000"}
		if($zsub1 > 450){
		$by3 = "FFFFFF"}else{$by3 = "FF0000"}
		if(($zname eq "안정" || $zname eq "무도" || $zname eq "검각" || $zname eq "자동" || $zname eq "건녕" || $zname eq "운남" || $zname eq "영안" || $zname eq "무릉" || $zname eq "영릉" || $zname eq "신야" || $zname eq "계양" || $zname eq "평원" || $zname eq "여강" || $zname eq "소패" || $zname eq "양평" || $zname eq "매소") && $zsub1 > 500){
		$by4 = "FFFFFF"}else{$by4 = "FF0000"}
		if($zsub1 > 750){
		$by5 = "FFFFFF"}else{$by5 = "FF0000"}
		if($zsub1 > 800){
		$by6 = "FFFFFF"}else{$by6 = "FF0000"}
		if($zsub1 > 1000){
		$by7 = "FFFFFF"}else{$by7 = "FF0000"}
		if(($zname eq "성도" || $zname eq "양양" || $zname eq "낙양" || $zname eq "허창" || $zname eq "장안" || $zname eq "업" || $zname eq "건업" || $zname eq "한") && $zsub1 > 1150){
		$by8 = "FFFFFF"}else{$by8 = "FF0000"}
		if($zname eq "운남" && $zsub1 > 750){
		$by9 = "FFFFFF"}else{$by9 = "FF0000"}
		if(($zname eq "서량" || $zname eq "안정" || $zname eq "계" || $zname eq "북평" || $zname eq "양평" || $zname eq "국내" || $zname eq "무도" || $zname eq "한중" || $zname eq "국내" || $zname eq "검각" || $zname eq "자동" || $zname eq "강주" || $zname eq "성도" || $zname eq "건녕" || $zname eq "영안" || $zname eq "서라벌" || $zname eq "졸본") && $zsub1 > 1150){
		$by10 = "FFFFFF"}else{$by10 = "FF0000"}
		if(($zname eq "서량" || $zname eq "안정" || $zname eq "계" || $zname eq "북평" || $zname eq "양평" || $zname eq "국내") && $zsub1 > 1100){
		$by11 = "FFFFFF"}else{$by11 = "FF0000"}
		if($zname eq "서라벌" && $zsub1 > 1100){
		$by12 = "FFFFFF"}else{$by12 = "FF0000"}
		if($zsub1 > 1199){
		$by13 = "FFFFFF"}else{$by13 = "FF0000"}
		if($zsub1 > 900){
		$by14 = "FFFFFF"}else{$by14 = "FF0000"}
		if($zname eq "회계" && $zsub1 > 899){
		$by15 = "FFFFFF"}else{$by15 = "FF0000"}
		if($zsub1 > 1199){
		$by16 = "FFFFFF"}else{$by16 = "FF0000"}
		if($zsub1 > 999){
		$by17 = "FFFFFF"}else{$by17 = "FF0000"}
		if($zsub1 > 749){
		$by18 = "FFFFFF"}else{$by18 = "FF0000"}
		if($zsub1 > 1099){
		$by19 = "FFFFFF"}else{$by19 = "FF0000"}


	print <<"EOM";
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
<body bgcolor="white" text="white" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" cellpadding="0" cellspacing="0" width="937">
    <tr>
        <td width="937">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="937" height="215" background="$IMG/backg.gif">
&nbsp;
            <table align="center" cellpadding="0" cellspacing="0" width="677">
                <tr>
                    <td width="677">
                        <p><img src="$IMG/law1.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="677" height="216" background="$IMG/law3.gif">
<center><TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>
<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>무력</TD><TH>$kstrt</TH><TD>지력</TD><TH>$kintt</TH><TD>통솔력</TD><TH>$kleat</TH></TR>
<TR><TD>금</TD><TH>$kgold</TH><TD>쌀</TD><TH>$krice</TH><TD>공헌</TD><TH>$kcex</TH></TR>
<TR><TD>현재위치</TD><TH colspan=2>$zname성</TH><TD>병사</TD><TH>$ksol</TH><TD>훈련</TD><TH>$kgat</TH></TR>
</TBODY></TABLE><br>

<table align="center" cellpadding="0" cellspacing="0" width="435" height="200" background="$IMG/get_sol.jpg">
    <tr>
        <td>
            <div align="right">
                <table cellpadding="0" cellspacing="0" width="328" height="200" bordercolordark="black" bordercolorlight="black">
                    <tr>
                        <td width="328" height="76" colspan="5">
                        </td>
                    </tr>
                    <tr>
                        <td width="80" valign="up">
                            <p align="center"><span style="font-size:9pt;"><a href="http://chilrang.cafe24.com/sam/command.cgi#1">보병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#2">궁병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#4">중장보병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#11">산악병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#15">황건적</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#19">수병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#20">공병</a></span></p>
                        </td>
                        <td width="80" valign="up">
                            <p align="center"><span style="font-size:9pt;"><a href="http://chilrang.cafe24.com/sam/command.cgi#6">기병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#10">코끼리병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#12">철기병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#13">화랑</a></span></p>
                        </td>
                        <td width="81" valign="up">
                            <p align="center"><span style="font-size:9pt;"><a href="http://chilrang.cafe24.com/sam/command.cgi#3">창병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#5">농민병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#7">의병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#16">산월병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#18">극병</a></span></p>
                        </td>
                        <td width="79" valign="up">
                            <p align="center"><span style="font-size:9pt;"><a href="http://chilrang.cafe24.com/sam/command.cgi#8">신귀병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#9">황실근위병</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#14">발석거</a><br><a href="http://chilrang.cafe24.com/sam/command.cgi#17">파쇄차</a></span></p>
                        </td>
                        <td width="8" valign="up">
                        </td>
                    </tr>
                </table>
            </div>
        </td>
    </tr>
</table>

<br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><span style="font-size:10pt;"><b><a name="1"></a>보병</b></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">보병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">평지 
                                    100% 수상 100% 산악 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max0</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">10</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">보병은 
                                    삼모전의 기본적인 클래스입니다. 싼 가격에 
                                    공격력 수비력, 성공격력마저도 없지만 무력에 
                                    자신이 있고 상대병력이 적다면&nbsp;써볼만한 
                                    유닛입니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
<p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=0><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by1"><span style="font-size:10pt;"><b><a name="2"></a>궁병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">보병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">평지 
                                    95% 수상 100% </font><font color="#00CC00">산악 115%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max1</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">10</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">보병보다 
                                    약간은 좋은 유닛입니다. 하지만 보병과는 
                                    다른 점은 거의 없지만 성공격력이 좋은 편입니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=1><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by2"><span style="font-size:10pt;"><b><a name="3"></a>창병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">창병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★(15)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★(45)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(10)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">평지 
                                    90%</font><font color="blue"> 수상 100% </font><font color="#00CC00">산악 120%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max2</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">20</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">창병은 
                                    싼가격에 만족할만한 수비력을 갖추고 있습니다. 
                                    게다가 산악에서 특화되어 산악에서 수비를 
                                    할시 특화된 수비력을 가지고 있습니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=2><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by3"><span style="font-size:10pt;"><b><a name="4"></a>중장보병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">보병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">평지 
                                    100% </font><font color="#00CC00">수상 120%</font><font color="blue"> 산악 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max3</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">20</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">중장보병은 
                                    전천후유닛입니다. 게다가 지형상성도 딱히 
                                    떨어지는 구석이 없어 어디서든지 사용하기 
                                    편리한 유닛입니다. 하지만 어느 한구석 뛰어난 
                                    구석도 없어서 애매한 유닛입니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=3><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by4"><span style="font-size:10pt;"><b><a name="5"></a>농민병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">창병계열</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">창병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">민심이 
                                    수비력에 가산</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">평지 
                                    100% </font><font color="#CC3300">수상 90%</font><font color="blue"> 산악 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max16</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">20</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">농민병은 
                                    자국이 수비하기 불리할 시 유용하게 쓰일 
                                    수 있는 유닛입니다. 수비력에 무려 민심이 
                                    가산되기 때문에 해당지역의 민심만 높다면 
                                    효과적으로 막아낼 수 있습니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=16><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by5"><span style="font-size:10pt;"><b><a name="6"></a>기병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">기병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★★(60)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★(15)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#00CC00">평지 
                                    130%</font><font color="blue"> </font><font color="#CC3300">수상 90% 산악 70%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max4</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">30</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">기병은 
                                    공격에 특화되었습니다. 특히 지형이 평지라면 
                                    강력한 힘을 발휘합니다. 하지만 수비와 성벽에 
                                    취약한 모습을 보입니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=4><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by6"><span style="font-size:10pt;"><b><a name="7"></a>의병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">창병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★☆(20)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">통솔이 
                                    가산</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★(45)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">평지 
                                    80%</font><font color="blue"> </font><font color="#00CC00">수상 110%</font><font color="blue"> 산악 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max6</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">40</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">의병은 
                                    두려운 유닛입니다. 수비에 통솔이 가산되기 
                                    때문에 통솔이 높은 장수라면 많은 병력과 
                                    더불어 적의 공격을 용납하지 않기 때문입니다. 
                                    공격력과 성공격력도 발군이어서 공격으로 
                                    전환해도 쓸만한 유닛입니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=6><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by7"><span style="font-size:10pt;"><b><a name="8"></a>신귀병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">귀병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">지력이 
                                    가산</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★(15)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">지력/2 
                                    가산</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">평지 
                                    100% </font><font color="#00CC00">수상 110%</font><font color="blue"> </font><font color="#CC3300">산악 90%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max5</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">40</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">지장을 
                                    위한 특화 유닛입니다. 공격력에 지력이 가산되어 
                                    비록 무력이 약한 지장이어도 충분히 강력한 
                                    힘을 발휘할 수 있습니다. 하지만 고용금이 
                                    비싸서 지속적인 전쟁참여가 어렵습니다. 스킬 
                                    「신출귀몰」을 사용할 수 있고 함정을 전부 피할 수 있습니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=5><input type=hidden name=mode value=10>$BUYBTN5
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by8"><span style="font-size:10pt;"><b><a name="9"></a>황실근위병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">귀병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">지력+매력 
                                    가산</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">무력+매력 
                                    가산</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">매력이 
                                    가산</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">평지 
                                    90%</font><font color="blue"> 수상 100% 산악 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max7</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">50</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">삼모전을 
                                    통틀어 최강의 유닛입니다. 공격력,수비력,성공격력 
                                    전부 통솔을 제외한 능력치가 반영이 됩니다. 
                                    공수를 통틀어 강력한 유닛입니다. 전술 「원공진」을 
                                    사용할 수 있습니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=7><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by9"><span style="font-size:10pt;"><b><a name="10"></a>코끼리병</b></span></font></p>
                                </td>
                            </tr>
                                 <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">기병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★★★★(90)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★★★★(90)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★★★(75)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#00CC00">평지 
                                    120%</font><font color="blue"> </font><font color="#CC3300">수상 
                                    80% 산악 70%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max8</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">60</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">코끼리병은 
                                    운남성에서만 징병가능한 유닛입니다. 하지만 
                                    공격력,수비력,성공격력은 발군의 성능을 자랑합니다. 
                                    단지 지형상성을 많이 타고 쌀소모가 극심합니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=8><input type=hidden name=mode value=10>$BUYBTN8
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by10"><span style="font-size:10pt;"><b><a name="11"></a>산악병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">보병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★(45)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★(45)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">평지 80% 수상 80%</font><font color="blue"> </font><font color="#00CC00">산악 130%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max9</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">30</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">산악병은 
                                    산악에서 뽑을 수 있는 산악 지형 전용 특화 
                                    유닛입니다. 공격력 수비력은 중장보병과 다를 
                                    게 없지만 산악지형에서 무려 2배의 지형상성이 
                                    붙습니다. 게다가 산악지형에서 스킬 「매복」을 
                                    사용할 수 있게 됩니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=9><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by11"><span style="font-size:10pt;"><b><a name="12"></a>철기병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">기병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★★★(75)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★★(60)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#00CC00">평지 
                                    130%</font><font color="blue"> </font><font color="#CC3300">수상 70% 산악 60%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max10</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">40</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">철기병은 
                                    북부 일부 도시에서만 생산이 가능합니다. 
                                    기존의 기병에서 철갑을 덧입혀 방어력이 강화되었습니다. 
                                    평지에서 발군의 성능을 자랑합니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=10><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by12"><span style="font-size:10pt;"><b><a name="13"></a>화랑</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">기병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">능력치 중에 한 가지 무작위</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">능력치 중에 한 가지 무작위</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">능력치 중에 한 가지 무작위</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">평지 
                                    90% 수상 90%</font><font color="blue"> 산악 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max11</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">30</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">화랑은 
                                    서라벌성에서만 뽑을 수 있는 유닛입니다. 
                                    성능이 랜덤하기 때문에 그 때 그 때마다 공격력,수비력,성공격력이 
                                    변화합니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=11><input type=hidden name=mode value=10>$BUYBTN11
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by13"><span style="font-size:10pt;"><b><a name="14"></a>발석거</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">귀병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★★★★★★★★(150)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">평지 
                                    100% 수상 100% 산악 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max12</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">40</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">발석거는 
                                    성점령에 있어 필수적인 존재입니다. 적의 
                                    성을 떨어뜨리는데 있어 발석거만큼 신속한 
                                    유닛은 없기 때문입니다. 하지만 대인전에서는 
                                    취약한 면모를 나타냅니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=12><input type=hidden name=mode value=10>$BUYBTN12
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by14"><span style="font-size:10pt;"><b><a name="15"></a>황건적</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">보병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">매력이 
                                    가산</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★(15)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">매력/2 
                                    가산</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#00CC00">평지 
                                    110%</font><font color="blue"> 수상 100% </font><font color="#CC3300">산악 80%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max13</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">30</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">지장에겐 
                                    신귀병이 있다면 매장에겐 황건적이 있습니다.&nbsp;공격력에 
                                    매력이 가산되기 때문에 매장에게는 특별한 
                                    매리트가 있습니다. 게다가 신귀병보다도 싸기 
                                    때문에 부담없이 사용할 수 있습니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=13><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by15"><span style="font-size:10pt;"><b><a name="16"></a>산월병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">창병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">무력이 
                                    가산</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★(15)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">무력/2 
                                    가산</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">평지 
                                    90%</font><font color="blue"> 수상 100% </font><font color="#00CC00">산악 110%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max15</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">30</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">산월병은 
                                    회계성에서만 뽑을 수 있는 지형 특화유닛입니다. 
                                    기존 무력+공격력 무력이 가산에서 발휘되는 
                                    공격력은 가공할 수준입니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value=15><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by16"><span style="font-size:10pt;"><b><a name="17"></a>파쇄차</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">귀병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★★★(75) 
                                    / 방어시설공격:★(10)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">평지 
                                    100% 수상 100% 산악 100%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max17</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">40</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">파쇄차는 
                                    발석거와는 달리 성벽을 공격할 뿐만 아니라 
                                    방어시설을 파괴합니다. 주로 공략하기가 쉽지 
                                    않는 특성이나 대성에 사용하여 농성수비대의 
                                    공격력을 약화시키는데 탁월합니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value="17"><input type=hidden name=mode value=10>$BUYBTN17
</form>
                                </td>
                            </tr>
                        </table>
			<br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by17"><span style="font-size:10pt;"><b><a name="18"></a>극병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">창병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">통솔이 
                                    가산</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">☆(0)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★(15)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">평지 
                                    100% </font><font color="#CC3300">수상 80%</font><font color="blue"> </font><font color="#00CC00">산악 110%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max18</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">40</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">극을 
                                    사용하는 부대입니다. 통솔력이 공격력에 가산되어 
                                    발군의 성능을 자랑합니다. 하지만 대인전을 
                                    제외하고는 그다지 쓸모가 있지는 않습니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value="18"><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table><br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by18"><span style="font-size:10pt;"><b><a name="19"></a>수병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">보병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★★(60)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★(45)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="#CC3300">평지 80% </font><font color="#00CC00">수상 130%</font><font color="blue"> </font><font color="#CC3300">산악 80%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max19</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">30</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">수상에서 
                                    전문적으로 싸우는 수병입니다. 고용금이 비싸긴 
                                    하지만 공격력과 수비력이 생각보다 괜찮지만 
                                    수상을 제외한 모든 지역에서는 불리한 병종입니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value="19"><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table>
			<br>
                        <table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
                            <tr>
                                <td width="432" height="35" colspan="2" bgcolor="black">
                                    <p align="center"><font color="$by19"><span style="font-size:10pt;"><b><a name="20"></a>공병</b></span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">병과</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">보병계열</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">수비력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★(30)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">성공격력</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">★★★(45)</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">지형상성</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="blue">평지 
                                    100% </font><font color="#00CC00">수상 110%</font><font color="blue"> </font><font color="#CC3300">산악 90%</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">고용금(30명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">$max20</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="20" bgcolor="black">
                                    <p><span style="font-size:9pt;">전쟁시 쌀소모(60명당)</span></p>
                                </td>
                                <td width="300" height="20" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">20</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="128" height="65" bgcolor="black">
                                    <p align="center"><span style="font-size:9pt;">설명</span></p>
                                </td>
                                <td width="300" height="65" bgcolor="#666666">
                                    <p><span style="font-size:9pt;"><font color="black">공병은 함정을 전문으로 해제하는 병종입니다. 공격력과 수비력이 중장보병수준에 불과하지만 함정을 해제하는 능력을 가지고 있습니다. 병력이 2000명이상을 100% 기준으로 그 이하는 많으면 많을수록 함정을 해제확률이 상승합니다. 또한 요격중인 적 수비부대의 공격력이 자신의 공격력의 2배이상일 경우 적의 수비력을 자신의 공격력으로 카피(Copy)합니다.</font></span></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="432" height="22" colspan="2" bgcolor="black">
<form action="$COMMAND" method="POST">
                                        <p align="right"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>명을 
$no_list<input type=hidden name=type value="20"><input type=hidden name=mode value=10><input type=submit value="고용한다">
</form>
                                </td>
                            </tr>
                        </table>			<br>

<br>

$LOCK_NOTE
<table align="center" border="1" cellspacing="0" width="438" bordercolordark="white" bordercolorlight="black">
<tr><td width="432" height="35" colspan="3" bgcolor="black"><p align="center"><span style="font-size:10pt;"><b>추가 병종</b></span></p></td></tr>
<tr><td width="150" bgcolor="black"><p align="center"><span style="font-size:9pt;">병종</span></p></td><td width="100" bgcolor="black"><p align="center"><span style="font-size:9pt;">금</span></p></td><td width="182" bgcolor="black"><p align="center"><span style="font-size:9pt;">고용</span></p></td></tr>
<tr><td bgcolor="#666666"><p><span style="font-size:9pt;"><font color="black">정예보병</font></span></p></td><td bgcolor="#666666"><p align="center"><span style="font-size:9pt;"><font color="black">$max21</font></span></p></td><td bgcolor="black"><form action="$COMMAND" method="POST"><p align="center"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=text name=num value=$get_sol size=4>$no_list<input type=hidden name=type value="21"><input type=hidden name=mode value=10><input type=submit value="고용"></p></form></td></tr>
<tr><td bgcolor="#666666"><p><span style="font-size:9pt;"><font color="black">정예기병</font></span></p></td><td bgcolor="#666666"><p align="center"><span style="font-size:9pt;"><font color="black">$max22</font></span></p></td><td bgcolor="black"><form action="$COMMAND" method="POST"><p align="center"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=text name=num value=$get_sol size=4>$no_list<input type=hidden name=type value="22"><input type=hidden name=mode value=10><input type=submit value="고용"></p></form></td></tr>
<tr><td bgcolor="#666666"><p><span style="font-size:9pt;"><font color="black">노궁병</font></span></p></td><td bgcolor="#666666"><p align="center"><span style="font-size:9pt;"><font color="black">$max23</font></span></p></td><td bgcolor="black"><form action="$COMMAND" method="POST"><p align="center"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=text name=num value=$get_sol size=4>$no_list<input type=hidden name=type value="23"><input type=hidden name=mode value=10><input type=submit value="고용"></p></form></td></tr>
<tr><td bgcolor="#666666"><p><span style="font-size:9pt;"><font color="black">중갑기병</font></span></p></td><td bgcolor="#666666"><p align="center"><span style="font-size:9pt;"><font color="black">$max24</font></span></p></td><td bgcolor="black"><form action="$COMMAND" method="POST"><p align="center"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=text name=num value=$get_sol size=4>$no_list<input type=hidden name=type value="24"><input type=hidden name=mode value=10><input type=submit value="고용"></p></form></td></tr>
<tr><td bgcolor="#666666"><p><span style="font-size:9pt;"><font color="black">창기병</font></span></p></td><td bgcolor="#666666"><p align="center"><span style="font-size:9pt;"><font color="black">$max25</font></span></p></td><td bgcolor="black"><form action="$COMMAND" method="POST"><p align="center"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=text name=num value=$get_sol size=4>$no_list<input type=hidden name=type value="25"><input type=hidden name=mode value=10><input type=submit value="고용"></p></form></td></tr>
<tr><td bgcolor="#666666"><p><span style="font-size:9pt;"><font color="black">투석병</font></span></p></td><td bgcolor="#666666"><p align="center"><span style="font-size:9pt;"><font color="black">$max26</font></span></p></td><td bgcolor="black"><form action="$COMMAND" method="POST"><p align="center"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=text name=num value=$get_sol size=4>$no_list<input type=hidden name=type value="26"><input type=hidden name=mode value=10><input type=submit value="고용"></p></form></td></tr>
<tr><td bgcolor="#666666"><p><span style="font-size:9pt;"><font color="black">화공병</font></span></p></td><td bgcolor="#666666"><p align="center"><span style="font-size:9pt;"><font color="black">$max27</font></span></p></td><td bgcolor="black"><form action="$COMMAND" method="POST"><p align="center"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=text name=num value=$get_sol size=4>$no_list<input type=hidden name=type value="27"><input type=hidden name=mode value=10><input type=submit value="고용"></p></form></td></tr>
<tr><td bgcolor="#666666"><p><span style="font-size:9pt;"><font color="black">친위대</font></span></p></td><td bgcolor="#666666"><p align="center"><span style="font-size:9pt;"><font color="black">$max28</font></span></p></td><td bgcolor="black"><form action="$COMMAND" method="POST"><p align="center"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=text name=num value=$get_sol size=4>$no_list<input type=hidden name=type value="28"><input type=hidden name=mode value=10><input type=submit value="고용"></p></form></td></tr>
<tr><td bgcolor="#666666"><p><span style="font-size:9pt;"><font color="black">산악병</font></span></p></td><td bgcolor="#666666"><p align="center"><span style="font-size:9pt;"><font color="black">$max29</font></span></p></td><td bgcolor="black"><form action="$COMMAND" method="POST"><p align="center"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=text name=num value=$get_sol size=4>$no_list<input type=hidden name=type value="29"><input type=hidden name=mode value=10><input type=submit value="고용"></p></form></td></tr>
<tr><td bgcolor="#666666"><p><span style="font-size:9pt;"><font color="black">수군</font></span></p></td><td bgcolor="#666666"><p align="center"><span style="font-size:9pt;"><font color="black">$max30</font></span></p></td><td bgcolor="black"><form action="$COMMAND" method="POST"><p align="center"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=text name=num value=$get_sol size=4>$no_list<input type=hidden name=type value="30"><input type=hidden name=mode value=10><input type=submit value="고용"></p></form></td></tr>
</table>
<form action="$FILE_STATUS" method="post">
                            <p align="center"><input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="돌아온다"></center></form>
                    </td>
                </tr>
                <tr>
                    <td width="677">
                        <p><img src="$IMG/law2.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
    <tr>
        <td width="937">
            <p><img src="$IMG/down.gif" width="950" height="26" border="0"></p>
        </td>
    </tr>
</table>
</body>

EOM
&FOOTER;
exit;

}
1;