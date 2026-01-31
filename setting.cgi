#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

&DECODE;
if( $in{'mode'} eq "edit" ){
	&EDIT;
}elsif( $in{'mode'} eq "passwd" ){
	&PASSWD;
}else{
	&TOP;
}

sub TOP {

	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);
	&CHARA_ITEM_OPEN;

	if( $in{'ins'} ne ""){
		$mes = $in{'ins'};
		$mes =~ s/<br>/\n/ig;
	}else{
		$mes = $kmes;
		$mes =~ s/<br>/\n/ig;
	}

	&HEADER;


	if($kskill =~ /Gb/){
	$ctotal = int((500+($kclass/50)) * 1.2);
	}else{
	$ctotal = 500+int($kclass/50);
	}

	open(IN,"./charalog/command1/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	foreach(@COM_DATA){
	($cname,$cno,$cp,$crap)=split(/<>/);
		$cpoin += $cp;
	}

	print <<"EOM";

	<script language="JavaScript">
		function changeImg(){
			num=document.para.mode.selectedIndex;
			document.Img.src="$IMG/jensul"+ num +".jpg";
		}
	</script>
<body bgcolor="white" text="white" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" cellpadding="0" cellspacing="0" width="945">
    <tr>
        <td width="945">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="945" height="740" background="$IMG/backg.gif">
            <table align="center" cellpadding="0" cellspacing="0" width="700">
                <tr>
                    <td width="940">
<p align="center">&nbsp;</p>
                        <p><img src="$IMG/law1.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="940" height="522" background="$IMG/law3.gif">
                            <table align="center" border="1" cellspacing="0" width="694" bordercolordark="white" bordercolorlight="black">
                                <tr>
                                    <td  width=200 height="424" rowspan="2">
EOM

	open(IN,"./charalog/command1/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

for($i=0;$i<30;$i++){
($cname,$cno,$cp,$crap) = split(/<>/,$COM_DATA[$i]);
		$no = $i+1;
		if($cno eq "" || $cno eq 0){
			$com_list .= "<TR height=20><TH width=30>$no턴</TH><TH width=100>일반공격</TH></TR>";
		}else{
			$com_list .= "<TR height=20><TH width=30>$no턴</TH><TH width=100>$cname</TH></TR>";
		}
	}

print <<"EOM";


<TABLE bgcolor=$TABLE_C cellspacing=1><TBODY BGCOLOR=$TD_C2>
<TR><th colspan=2>전술 입력 커맨드</th></TR>
<TR><th colspan=2>포인트 $cpoin/$ctotal</th></TR>
$com_list
</TABLE>
                                    </td>

<form action="./command1.cgi" method="POST" name=para>
                                    <td width="479" height="13">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>

<table>
    <tr>
        <td rowspan="2">
<select name=no size="6" MULTIPLE style="color:rgb(204,204,0); background-color:rgb(93,40,0);">
<option value="all">ALL
EOM
	for($i=0;$i<30;$i++){
		$no = $i+1;
		if($i eq "0"){
		print "<option value=\"$i\" SELECTED>$no턴";
		}else{
		print "<option value=\"$i\">$no턴";
		}
	}
print <<"EOM";
</select>
        </td>
        <td colspan="2">
<p align="center"><img src=\"$IMG/jensul0.jpg\" name=\"Img\"></p>
        </td>
    </tr>
    <tr>
        <td>
<select name=mode style="font-size:9pt;" onChange=\"changeImg()\" size=1>
<option value="0">일반공격
<option style="color:#000000;background-color:#C7FFC9;" value="1">추행진 [관통(가위) / 승10% / 패10% / CP25]
<option style="color:#000000;background-color:#C7FFC9;" value="2">원진 [밀집(바위) / 승10% / 패10% / CP25]
<option style="color:#000000;background-color:#C7FFC9;" value="3">장사진 [분산(보) / 승10% / 패10% / CP25]
<option style="color:#000000;background-color:#AEAE48;" value="4">어린진 [관통(가위) / 승15% / 패12% / CP75]
<option style="color:#000000;background-color:#AEAE48;" value="5">방원진 [밀집(바위) / 승15% / 패12% / CP75]
<option style="color:#000000;background-color:#AEAE48;" value="6">안행진 [분산(보) / 승15% / 패12% / CP75]
<option style="color:#000000;background-color:#CC3399;" value="14">신출귀진 [관통(가위) / 승20% / 패12% / CP100 / 신귀병]
<option style="color:#000000;background-color:#CC3399;" value="11">열화진 [관통(가위) / 승28% / 패15% / CP150 / 오화신염선]
<option style="color:#000000;background-color:#CC3399;" value="12">비천진 [밀집(바위) / 승18% / 패12% / CP170 / 천극도 / 수비시 적공격↓]
<option style="color:#000000;background-color:#CC3399;" value="16">원공진 [밀집(바위) / 승15% / 패8% / CP300 / 황근병 / 수비시 병력회복]
<option style="color:#000000;background-color:#CC3399;" value="13">탄망진 [분산(보) / 승22% / 패15% / CP150 / 백귀난마 / 적피로도↑]
<option style="color:#000000;background-color:#CC3399;" value="15">신라검진 [분산(보) / 승15% / 패12% / CP120 / 화랑 / 훈련도 -5씩 하락]
</select>
        </td>
        <td>
<input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BC[$xele]; border-width:1; border-color:black; border-style:solid;" value="실행">
        </td>
</form>
    </tr>
</table>
                                    </td>
                                </tr>
                                <tr>
                                    <td width="550" height="411" valign="up">

<table border="1" width="100%">
    <tr>
        <td width="100%" border="0" cellspacing="1" cellpadding="2" bgcolor=black>
            <p><b>[전술 커맨드 시스템 이용방법]</b><br>자신의 주어진 전술포인트(CP)의 
            한도내에서 전술을 짭니다.<br>전술을 하나 추가할 때마다 펼침메뉴창에 
            표시된 CP만큼 소모되며 승리시 가산되는 지형상성퍼센트와 패배시 감산되는 
            지형상성퍼센트가 표시됩니다.<br>CP는 총경험치와 연관이 있으며 총경험치가 
            늘어날수록 구사할 수 있는 전술이 생겨납니다.<br>전술상성은 <b>관통(가위) 
            &gt;&nbsp;분산(보) &gt; 밀집(바위) &gt; 관통(가위) </b>이며 이기거나 
            지거나 비길 수 있습니다.<br>단, 일반공격은 모든 상성에게 반드시 패배하지만 적의 특수공격(스킬)의 영향을 받지 않습니다..<br><b>※CP는 한번쓰면 없어지는 소모성포인트가 아닙니다.</b></p>
        </td>
    </tr>
</table>
<br>
<form action="setting.cgi" method="post">
<input type=hidden name=mode value="edit">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
	<table width="100%" border="0" cellspacing="1" cellpadding="2" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
	<tr bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<td width="200">열전 자기소개<br>(전각 100자까지)</td>
	<td width="300">$kmes<br><textarea name="ins" cols="40" rows="5">$mes</textarea>
	</td>
	</tr>
    <tr>
	<td width="1105" colspan="2">
            <p align="center"><input type="submit" value="설정">
</td>
		</form>
    </tr>
	</table>
<br>
<form action="setting.cgi" method="post">
<input type=hidden name=mode value="passwd">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
	<table width="100%" border="0" cellspacing="1" cellpadding="2" bgcolor=$ELE_BG[$cou_ele[$kcon]]>
	<tr bgcolor=$ELE_C[$cou_ele[$kcon]]>
	<td width="100">패스워드 변경</td>
	<td width="308"><input type=text name=newpass value="" size="10" maxlength="8">[반각영숫자로 4~8문자 이내]
	</td>
	<td width="76">
<input type="submit" value="설정">
	</td>
</form>
	</tr>
	</table>
<br>
<form action="backup.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=BAK>
<p align="center"><input type=submit value="데이터백업(하루에 한번씩 권장)"></p></form>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<p align="center"><input type=submit value="확인"></p></form>
                                    </td>
                                </tr>
                            </table>
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="940">
                        <p><img src="$IMG/law2.gif" width="700" height="22" border="0"></p>
                    </td>
                </tr>
            </table>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td width="945">
            <p><img src="$IMG/down.gif" width="950" height="26" border="0"></p>
        </td>
    </tr>
</table>
</body>

EOM

	&FOOTER;
	exit;

}

sub EDIT {
	&CHARA_MAIN_OPEN;

	$ins = $in{'ins'};
	if( length($ins) > 200){
		&TOP("에러 : 전각 100자를 넘어버렸습니다.");
	}
	$kmes = $ins;
	&CHARA_MAIN_INPUT;

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>설정을 완료했습니다.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인"></form></CENTER>
EOM

	&FOOTER;
	exit;

}

sub BAK {
	&CHARA_MAIN_OPEN;

	open(IN,"./charalog/bak/$in{'id'}.cgi");
	@KK = <IN>;
	close(IN);

	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct,$klevel,$kexp,$kcodea,$kcodeb,$kqpoint) = split(/<>/);

	open(OUT,">./charalog/bak/$in{'id'}.cgi");
	print OUT @KK;
	close(OUT);

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$in{'id'}님의 데이터를 백업했습니다.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인"></form></CENTER>

EOM

	&FOOTER;
	exit;
}




sub PASSWD {
	&CHARA_MAIN_OPEN;

	if ($in{'newpass'} =~ m/[^0-9a-zA-Z]/) {&TOP("","에러 : 패스워드에 반각영숫자 이외의 문자가 포함되어 있습니다."); }
	elsif($in{'newpass'} eq "" || length($in{'newpass'}) < 4 || length($in{'newpass'}) > 8) { &TOP("","에러 : 4문자 이상 8문자 이하로 입력해주세요."); }
	$kpass = $in{'newpass'};
	&CHARA_MAIN_INPUT;

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>패스워드를 변경했습니다.</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인"></form></CENTER>

EOM

	&FOOTER;
	exit;

}


