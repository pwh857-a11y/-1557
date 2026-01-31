#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';
&COUNTRY_DATA_OPEN($kcon);
if($MENTE) { &ERR2("로딩중입니다. 잠시만 기다려 주세요."); }
&DECODE;
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("주소 바에 값을 입력하지 마세요."); }
if($mode eq 'C_RAN') { &C_RAN; }
else{&RANKING;}



sub RANKING {

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	$num = @CL_DATA;
	$i=0;
	$date = time;


	&SERVER_STOP;

	&HEADER;


	print <<"EOM";
<body bgcolor="white" text="white" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" cellpadding="0" cellspacing="0" width="945">
    <tr>
        <td width="945">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="945" height="600" background="$IMG/backg.gif">
            <table align="center" cellpadding="0" cellspacing="0" width="933" height="100%">
                <tr>
                    <td width="220" valign="up">
EOM

	$c_c=0;
	$c_i=0;
	foreach(@COU_DATA){
		($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
		if($xking ne "" && $c_k_name[$c_c] eq ""){
			open(IN,"./charalog/main/$xking.cgi");
			@CN_DATA = <IN>;
			close(IN);
			($lid,$lpass,$lname) = split(/<>/,$CN_DATA[0]);
			$c_k_name[$c_c] = "$lname";
		}
print<<"EOM";
<a href="./$FILE_RANK?mode=C_RAN&con_no=$xcid" target="a"><img src="$IMG/bot[$xele].jpg" width="260" height="50" border="0"></a>
EOM
		$c_c++;
		$c_i++;
	}
print<<"EOM";
<a href="./$FILE_RANK?mode=C_RAN&con_no=0" target="a"><img src="$IMG/bot[0].jpg" width="260" height="50" border="0"></a>
                    </td>
                    <td width="713" rowspan="2">
<IFRAME  FRAMEBORDER=no SCROLLING=yes WIDTH=100% HEIGHT=100% SRC="./$FILE_RANK?mode=C_RAN&con_no=$xcid" name='a'></IFRAME>
                    </td>
                </tr>
                <tr>
                    <td width="220" align="center" valign="bottom">
총장수:$num명<br>
<form action="$FILE_TOP" method="post"><input type=submit style="font-family:궁서; color:rgb(204,255,0); background-color:rgb(153,102,0);" value="메뉴로 돌아온다."></form>
                    </td>
                </tr>
            </table>
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


sub C_RAN{

	open(IN,"$CHARA_DATA");
	@DL_DATA = <IN>;
	close(IN);

	open(IN,"$ARM_LIST");
	@ARM_DATA = <IN>;
	close(IN);
	($armname,$armval,$armdmg,$armwei,$armele,$armsta,$armclass,$armtownid) = split(/<>/,$ARM_DATA[$cnum]);
	
	open(IN,"$COUNTRY_LIST") or &ERR2('파일을 열지 않았습니다.');
	@COU_DATA = <IN>;
	close(IN);
	$country_no=0;

	foreach(@COU_DATA){
		($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
		if($xcid eq $in{'con_no'}){
		$couname="$xname";
		$c[$country_no]=0;
		$c_no[$country_no]=$xcid;
		$couking=$xking;
		($x0,$x1,$x2,$x3,$x4,$x5,$x6,$x7,$x8,$x9,$x10,$x11,$x12,$x13,$x14,$x15,$x16,$x17,$x18,$x19,$x20,$x21,$x22,$x23,$x24,$x25,$x26,$xxsub1,$xxsub2)= split(/,/,$xsub);
		$coux0=$x0;
		$coux1=$x1;
		$coux17=$x17;
		}
	}

	open(IN,"$TOWN_LIST");
	@T_LIST = <IN>;
	close(IN);
	$town_c0=0;$town_c1=0;$town_c2=0;$town_c3=0;
	$l=0;
	$dosi=0;
	foreach(@T_LIST){
		($zname,$zcon,$znum,$znou,$zsyo,$zshiro,$znou_max,$zsyo_max,$zshiro_max,$zpri,$zx,$zy,$zsouba,$z[0],$z[1],$z[2],$z[3])=split(/<>/);
			if($zcon eq $in{'con_no'}){$dosi++;}
	}

	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro)=split(/<>/);
		if($z2con eq $zcon){
				$zsyo_sal += int($z2syo * 8 * $z2num / 10000);
				$znou_sal += int($z2nou * 8 * $z2num / 10000);
		}
	}

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	@tmp = map {(split /<>/)[14]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$good=0;
	foreach(@CL_DATA) {
	($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct,$klevel,$kexp,$kcodea,$kcodeb,$kqpoint) = split(/<>/);
		$chit=0;
			if($kcon eq "" || $kcon eq "0"){
			$chit=1;
			}
			if($kcon eq "$in{'con_no'}"){
				if($kid eq "$couking"){
					$couking1 = $kname;
				}
				if($kid eq "$coux0"){
					$coux01 = $kname;
				}
				if($kid eq "$coux1"){
					$coux11 = $kname;
				}
				if($kid eq "$coux17"){
					$coux171 = $kname;
				}
				if($c[$j] <= 70 && $kcon ne 0){
				$ldate = $DEL_TURN - $ksub2;
				if($ldate <= 0){
					$rm = "<font color=red>삭제 대상</font>";
				}else{
					$rm = "<font color=blue>$ldate</font>";
				}
				$list[$j] .= "<TR><TD><img src=$IMG/$kchara.gif></TD><TD><center><a href=\"javascript:info('$kid')\">$kname</a></TD><TD><center>$kstr</TD><TD><center>$kint</TD><TD><center>$klea</TD><TD><center>$kcha</TD><TD><center>Lv.$klevel</TD><TD><center>$rm턴</TD></TR>";
				}else{
					$lista[$j] .= "$kname【Lv.$s_num】 ";
				}
				$good++;
			}
			
			if($kcon eq "" || $kcon eq "0"){
				$ldate = $DEL_TURN - $ksub2;
				if($ldate <= 0){
					$rm = "<font color=red>삭제 대상</font>";
				}else{
					$rm = "<font color=blue>$ldate</font>";
				}
				$jaeya .="<TR><TD><img src=$IMG/$kchara.gif></TD><TD><center><a href=\"javascript:info('$kid')\">$kname</a></TD><TD><center>$kstr</TD><TD><center>$kint</TD><TD><center>$klea</TD><TD><center>$kcha</TD><TD><center>Lv.$klevel</TD><TD><center>$rm턴</TD></TR>";
				$good1++;
			}

	}


	&SERVER_STOP;

	$C_NEXT_NUM = 100;

	&HEADER1;
	$l_rank = "<TR width=60%><TD></TD><TH width=70>이름</TH><TH width=50>무력</TH><TH width=50>지력</TH><TH width=50>통솔력</TH><TH width=50>매력</TH><TH width=80>레벨</TH><TH width=100>삭제남은 기간</TH></TR>";



	$c_c=0;
	if($in{'con_no'} ne "0"){

		foreach(@COU_DATA){
		($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
			if($xcid eq $in{'con_no'}){
			if($xking ne "" && $c_k_name[$c_c] eq ""){
				open(IN,"./charalog/main/$xking.cgi");
				@CN_DATA = <IN>;
				close(IN);
				($lid,$lpass,$lname) = split(/<>/,$CN_DATA[0]);
				$c_k_name[$c_c] = "$lname";
			}
	print<<"EOM";
<body background="$IMG/backg.gif">
<table align="center" cellpadding="0" cellspacing="0" width="540" height="180" bordercolordark="white" bordercolorlight="black" background="$IMG/rank[$xele].gif">
    <tr>
        <td width="1101">
            <table cellpadding="0" cellspacing="0" width="516">
                <tr align="left" valign="top">
                    <td width="95" height="186" rowspan="5">
                        <p></p>
                    </td>
                    <td width="421" height="34" colspan="4">
                        <p></p>
                    </td>
                </tr>
                <tr>
                    <td width="89" height="34">
                        <p align="center"><font color="white" face="돋움"><span style="font-size:9pt;">$couking1</span></font></p>
                    </td>
                    <td width="86" height="34">
                        <p></p>
                    </td>
                    <td width="87" height="34">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$coux171</span></font></p>
                    </td>
                    <td width="158" height="112" rowspan="3">
                        <p></p>
                    </td>
                </tr>
                <tr>
                    <td width="89" height="45">
                        <p align="center"><font color="white" face="돋움"><span style="font-size:9pt;">$coux01</span></font></p>
                    </td>
                    <td width="86" height="45">
                        <p></p>
                    </td>
                    <td width="87" height="45">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$good명</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="89" height="33">
                        <p align="center"><font color="white" face="돋움"><span style="font-size:9pt;">$coux11</span></font></p>
                    </td>
                    <td width="86" height="33">
                        <p></p>
                    </td>
                    <td width="87" height="33">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$dosi도시</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="421" height="40" colspan="4">
                        <p></p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<BR>
	      <TABLE bgcolor=$ELE_BG[$xele] border="0" width=0% align=center>
	        <TBODY bgcolor=$ELE_C[$xele]>
	$l_rank $list[$c_c] 
	         </TR>
			<TR><TD bgcolor=$ELE_C[$xxele] align=center colspan=20><font color=$ELE_BG[$xxele]>$lista[0]
			</TD></TR>
	        </TBODY>
	      </TABLE>
EOM
			$c_c++;
			}
		}

	}else{

	$xele=0;

	print<<"EOM";
	<TABLE bgcolor=$ELE_BG[$xxele] width=100%><TBODY><TR><TD colspan=2 bgcolor=$ELE_BG[$xele] align=center><font color=$ELE_C[$xele] size=4><B>장수</font></TD></TR><TR><TD bgcolor=$ELE_C[$xele]><font color=$ELE_BG[$xele]>장수수</TD><TD bgcolor=$ELE_C[$xele]><font color=$ELE_BG[$xele]> $good1 명</TD></TR></TBODY></TABLE><BR>
	      <TABLE bgcolor=$ELE_BG[$xele] border="0" align="center">
	        <TBODY bgcolor=$ELE_C[$xele]>
	$l_rank $jaeya
	         </TR>
	        </TBODY>
	      </TABLE>
EOM
	}

	$q=0;
	for($p=0;$p<$c[0];$p+=$C_NEXT_NUM){
		$next_mes .= "\[<a href=./$FILE_RANK?mode=C_RAN&con_no=$in{'con_no'}&c_num=$p>$q</a>\] ";
		$q++;
	}
	
print <<"EOM";
$next_mes
EOM

	&FOOTER;

	exit;

}