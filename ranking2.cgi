#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR2("로딩중입니다. 잠시만 기다려 주세요."); }
&DECODE;
#if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("주소 바에 값을 입력하지 마세요."); }
&RANKING;

sub RANKING {

	&SERVER_STOP;
	open(IN,"$COUNTRY_NO_LIST") or &ERR2('파일을 열지 않았습니다.');
	@COU_DATA = <IN>;
	close(IN);
	$country_no=1;

	foreach(@COU_DATA){
		($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
		$cou_name[$country_no]="$xname";
		$country_no++;
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
			($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/,$page[0]);
			($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$ktec1,$ktec2,$ktec3,$kvsub1,$kvsub2,) = split(/,/,$ksub1);
			$lpoint = $kstr+$kint+$klea+$kcha;
			push(@CL_DATA,"$kid<>$kpass<>$kname<>$kchara<>$kstr<>$kint<>$klea<>$kcha<>$ksol<>$kgat<>$kcon<>$kgold<>$krice<>$kcex<>$kclass<>$karm<>$kbook<>$kbank<>$ksub1<>$ksub2<>$kpos<>$kmes<>$khost<>$kdate<>$kmail<>$kos<>$lpoint<>$ksub2_ex<>\n");
		}
	}
	closedir(dirlist);



	@tmp = map {(split /<>/)[26]} @CL_DATA;
	@POINT = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;

	foreach(@POINT){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint) = split(/<>/);
		if($cou_name[$kcon] eq ""){
			$kcon_name= "재야";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$bpoint = "$klpoint";
			$bpoint1 = "$kname";
			$bpoint2 = "$IMG/$kchara.gif";
			$bpoint3 = "$kcon_name";
			$point_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>무력:$kstr</b></p></td></tr><tr valign=up><td height=30 background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}else{
		$point_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>무력:$kstr</b></p></td></tr><tr valign=up><td height=30 background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[4]} @CL_DATA;
	@STR = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	foreach(@STR){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($kstr > 240){
		$bar = 120;
		}else{
		$bar=int($kstr/2);
		}
		if($cou_name[$kcon] eq ""){
			$kcon_name= "재야";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$bstr = "$kstr";
			$bstr1 = "$kname";
			$bstr2 = "$IMG/$kchara.gif";
			$bstr3 = "$kcon_name";
		$str_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>무력:$kstr</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}else{
		$str_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>무력:$kstr</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[5]} @CL_DATA;
	@INT = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	foreach(@INT){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($kint > 240){
		$bar = 120;
		}else{
		$bar=int($kint/2);
		}
		if($cou_name[$kcon] eq ""){
			$kcon_name= "재야";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$bint = "$kint";
			$bint1 = "$kname";
			$bint2 = "$IMG/$kchara.gif";
			$bint3 = "$kcon_name";
			$int_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>지력:$kint</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}else{
		$int_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국</a><br>지력:$kint</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[6]} @CL_DATA;
	@LER = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	foreach(@LER){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($klea > 240){
		$bar = 120;
		}else{
		$bar=int($klea/2);
		}
		if($cou_name[$kcon] eq ""){
			$kcon_name= "재야";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
		$lea_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>통솔:$klea</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
			$blea = "$klea";
			$blea1 = "$kname";
			$blea2 = "$IMG/$kchara.gif";
			$blea3 = "$kcon_name";
		}else{
		$lea_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>통솔:$klea</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[7]} @CL_DATA;
	@CHA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	foreach(@CHA){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($kcha > 240){
		$bar = 120;
		}else{
		$bar=int($kcha/2);
		}
		if($cou_name[$kcon] eq ""){
			$kcon_name= "재야";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$bcha = "$kcha";
			$bcha1 = "$kname";
			$bcha2 = "$IMG/$kchara.gif";
			$bcha3 = "$kcon_name";
		$cha_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>매력:$kcha</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}else{
		$cha_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>매력:$kcha</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[11]} @CL_DATA;
	@GOLD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	foreach(@GOLD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos) = split(/<>/);
		if($kgold > 360000){
		$bar = 120;
		}else{
		$bar=int($kgold/3000);
		}
		if($cou_name[$kcon] eq ""){
			$kcon_name= "재야";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$bgold = "$kgold";
			$bgold1 = "$kname";
			$bgold2 = "$IMG/$kchara.gif";
			$bgold3 = "$kcon_name";
		$gold_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>$kgold</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}else{
		$gold_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>$kgold</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[12]} @CL_DATA;
	@RICE = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	foreach(@RICE){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct,$klevel,$kexp,$kcodea,$kcodeb,$kqpoint) = split(/<>/);
		if($krice > 360000){
		$bar = 120;
		}else{
		$bar=int($krice/3000);
		}
		if($cou_name[$kcon] eq ""){
			$kcon_name= "재야";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$brice = "$krice";
			$brice1 = "$kname";
			$brice2 = "$IMG/$kchara.gif";
			$brice3 = "$kcon_name";
		$rice_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>$krice</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}else{
		$rice_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>$krice</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}
		$i++;
		if($i>10){last;}
	}


	@tmp = map {(split /<>/)[14]} @CL_DATA;
	@CLASS = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	foreach(@CLASS){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$kskill,$kpoint,$kct,$klevel,$kexp,$kcodea,$kcodeb,$kqpoint) = split(/<>/);
		if($kclass > 48000){
		$bar = 120;
		}else{
		$bar=int($kclass/400);
		}
		if($cou_name[$kcon] eq ""){
			$kcon_name= "재야";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($i eq 1){
			$bclass = "$kclass";
			$bclass1 = "$kname";
			$bclass2 = "$IMG/$kchara.gif";
			$bclass3 = "$kcon_name";
		$class_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>$kclass</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}else{
		$class_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>$kclass</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}
		$i++;
		if($i>10){last;}
	}

	@tmp = map {(split /<>/)[27]} @CL_DATA;
	@DEAD = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	$i=1;
	foreach(@DEAD){
		($kid,$kpass,$kname,$kchara,$kstr,$kint,$klea,$kcha,$ksol,$kgat,$kcon,$kgold,$krice,$kcex,$kclass,$karm,$kbook,$kbank,$ksub1,$ksub2,$kpos,$kmes,$khost,$kdate,$kmail,$kos,$klpoint,$knum) = split(/<>/);
		if($knum > 120){
		$bar = 120;
		}else{
		$bar=$knum;
		}
		if($cou_name[$kcon] eq ""){
			$kcon_name= "재야";
		}else{
			$kcon_name= "$cou_name[$kcon]";
		}
		if($knum eq ""){
			$knum=0;
		}
		if($i eq 1){
			$bnum = "$knum";
			$bnum1 = "$kname";
			$bnum2 = "$IMG/$kchara.gif";
			$bnum3 = "$kcon_name";
		$dead_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>사살:$knum</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}else{
		$dead_list .= "<td><table cellpadding=0 cellspacing=0 valign=bottom><tr><td bgcolor=#333333><p align=center><img src=$IMG/$kchara.gif border=0><br><b><a href=\"javascript:info('$kid')\">$kname</a><br>$kcon_name국<br>사살:$knum</b></p></td></tr><tr valign=up><td height=$bar background=$IMG/rangkingbar.jpg><p align=center><font color=black><b>$i위</b></font></p></td></tr></table></td>";
		}
		$i++;
		if($i>10){last;}
	}


	&HEADER;

	print <<"EOM";
$a
<BODY oncontextmenu="return false" onselectstart="return false" ondragstart="return false" bgcolor="black" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<body bgcolor="white" text="black" link="blue" vlink="purple" alink="red" leftmargin="0" marginwidth="0" topmargin="0" marginheight="0" background="$IMG/back.jpg">
<table align="center" cellpadding="0" cellspacing="0" width="950">
    <tr>
        <td width="1101">
            <p><img src="$IMG/up.gif" width="950" height="93" border="0"></p>
        </td>
    </tr>
    <tr>
        <td width="1101" height="1429" background="$IMG/backg.gif"><p align="center">
<br><img src="$IMG/b2.gif"><br><br>
<table align="center" cellpadding="0" cellspacing="0" width="540" height="500" bordercolordark="white" bordercolorlight="black" background="$IMG/rank.gif">
    <tr>
        <td width="1101">
            <table align="center" cellpadding="0" cellspacing="0" width="540" height="500" background="$IMG/rank.gif">
                <tr>
                    <td width="540" height="126" colspan="11">
                        <p align="center">&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="30" height="296" rowspan="5">
                        <p align="center">&nbsp;</p>
                    </td>
                    <td width="67" height="78">
                        <p align="center"><img src="$bpoint2" width="64" height="80" border="0"></p>
                    </td>
                    <td width="33" height="122" rowspan="2">
                        <p align="center">&nbsp;</p>
                    </td>
                    <td width="67" height="78">
                        <p align="center"><img src="$bstr2" width="64" height="80" border="0"></p>
                    </td>
                    <td width="37" height="122" rowspan="2">
                        <p align="center">&nbsp;</p>
                    </td>
                    <td width="68" height="78">
                        <p align="center"><img src="$bint2" width="64" height="80" border="0"></p>
                    </td>
                    <td width="38" height="122" rowspan="2">
                        <p align="center">&nbsp;</p>
                    </td>
                    <td width="68" height="78">
                        <p align="center"><img src="$blea2" width="64" height="80" border="0"></p>
                    </td>
                    <td width="36" height="122" rowspan="2">
                        <p align="center">&nbsp;</p>
                    </td>
                    <td width="68" height="78">
                        <p align="center"><img src="$bcha2" width="64" height="80" border="0"></p>
                    </td>
                    <td width="28" height="296" rowspan="5">
                        <p align="center">&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="67" height="48">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$bpoint3국<br> 
                        $bpoint1<br><b>총력:$bpoint</b><br></span></font></p>
                    </td>
                    <td width="67" height="48">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$bstr3국<br> 
                        $bstr1<br><b>무력:$bstr</b></span></font></p>
                    </td>
                    <td width="68" height="48">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$bint3국<br> 
                        $bint1<br><b>지력:$bint</b></span></font></p>
                    </td>
                    <td width="68" height="48">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$blea3국<br>
                        $blea1<br><b>통솔:$blea</b></span></font></p>
                    </td>
                    <td width="68" height="48">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$bcha3국<br>
                        $bcha1<br><b>매력:$bcha</b></span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="482" height="50" colspan="9">
                        <p align="center">&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="67" height="84">
                        <p align="center"><img src="$bgold2" width="64" height="80" border="0"></p>
                    </td>
                    <td width="33" height="119" rowspan="2">
                        <p align="center">&nbsp;</p>
                    </td>
                    <td width="67" height="84">
                        <p align="center"><img src="$brice2" width="64" height="80" border="0"></p>
                    </td>
                    <td width="37" height="119" rowspan="2">
                        <p align="center">&nbsp;</p>
                    </td>
                    <td width="68" height="84">
                        <p align="center"><img src="$bclass2" width="64" height="80" border="0"></p>
                    </td>
                    <td width="38" height="119" rowspan="2">
                        <p align="center">&nbsp;</p>
                    </td>
                    <td width="68" height="84">
                        <p align="center"><img src="$bnum2" width="64" height="80" border="0"></p>
                    </td>
                    <td width="104" height="119" rowspan="2" colspan="2">
                        <p align="center">&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="67" height="45">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$bgold3국<br> 
                        $bgold1<br><b>$bgold괴</b></span></font></p>
                    </td>
                    <td width="67" height="45">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$brice3국<br>
                        $brice1<br><b>$brice석</b></span></font></p>
                    </td>
                    <td width="68" height="45">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$bclass3국<br>
                        $bclass1<br><b>$bclass</b></span></font></p>
                    </td>
                    <td width="68" height="45">
                        <p align="center"><font color="white"><span style="font-size:9pt;">$bnum3국<br>
                        $bnum1<br><b>$bnum명</b></span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="540" colspan="11">
                        <p align="center">&nbsp;</p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br><br>
<table align="center" cellpadding="0" cellspacing="0" width="700" height="350">
    <tr>
        <td width="569" height="177" background="$IMG/rankingpyo.jpg">
            <table cellpadding="0" cellspacing="0" width="700" height="350">
                <tr>
                    <td width="690" height="38" colspan="2">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="34" height="45">
                        <p>&nbsp;</p>
                    </td>
                    <td width="665" height="45">
                        <p><span style="font-size:14pt;">칠랑서버 호걸 10 순위</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="239" colspan="2">
                        <table cellpadding="0" height=100% cellspacing="0" align="center">
                            <tr valign=bottom>
			    $str_list
				</tr>
			</table>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="28" colspan="2">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br><br>
<table align="center" cellpadding="0" cellspacing="0" width="700" height="350">
    <tr>
        <td width="569" height="177" background="$IMG/rankingpyo.jpg">
            <table cellpadding="0" cellspacing="0" width="700" height="350">
                <tr>
                    <td width="690" height="38" colspan="2">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="34" height="45">
                        <p>&nbsp;</p>
                    </td>
                    <td width="665" height="45">
                        <p><span style="font-size:14pt;">칠랑서버 수재 10 순위</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="239" colspan="2">
                        <table cellpadding="0" height=100% cellspacing="0" align="center">
                            <tr valign=bottom>
			    $int_list
				</tr>
			</table>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="28" colspan="2">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br><br>
<table align="center" cellpadding="0" cellspacing="0" width="700" height="350">
    <tr>
        <td width="569" height="177" background="$IMG/rankingpyo.jpg">
            <table cellpadding="0" cellspacing="0" width="700" height="350">
                <tr>
                    <td width="690" height="38" colspan="2">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="34" height="45">
                        <p>&nbsp;</p>
                    </td>
                    <td width="665" height="45">
                        <p><span style="font-size:14pt;">칠랑서버 지휘관 10 순위</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="239" colspan="2">
                        <table cellpadding="0" height=100% cellspacing="0" align="center">
                            <tr valign=bottom>
			    $lea_list
				</tr>
			</table>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="28" colspan="2">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br><br>
<table align="center" cellpadding="0" cellspacing="0" width="700" height="350">
    <tr>
        <td width="569" height="177" background="$IMG/rankingpyo.jpg">
            <table cellpadding="0" cellspacing="0" width="700" height="350">
                <tr>
                    <td width="690" height="38" colspan="2">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="34" height="45">
                        <p>&nbsp;</p>
                    </td>
                    <td width="665" height="45">
                        <p><span style="font-size:14pt;">칠랑서버 덕장 10 순위</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="239" colspan="2">
                        <table cellpadding="0" height=100% cellspacing="0" align="center">
                            <tr valign=bottom>
			    $cha_list
				</tr>
			</table>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="28" colspan="2">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br><br>
<table align="center" cellpadding="0" cellspacing="0" width="700" height="350">
    <tr>
        <td width="569" height="177" background="$IMG/rankingpyo.jpg">
            <table cellpadding="0" cellspacing="0" width="700" height="350">
                <tr>
                    <td width="690" height="38" colspan="2">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="34" height="45">
                        <p>&nbsp;</p>
                    </td>
                    <td width="665" height="45">
                        <p><span style="font-size:14pt;">칠랑서버 부호 10 순위</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="239" colspan="2">
                        <table cellpadding="0" height=100% cellspacing="0" align="center">
                            <tr valign=bottom>
			    $gold_list
				</tr>
			</table>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="28" colspan="2">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br><br>
<table align="center" cellpadding="0" cellspacing="0" width="700" height="350">
    <tr>
        <td width="569" height="177" background="$IMG/rankingpyo.jpg">
            <table cellpadding="0" cellspacing="0" width="700" height="350">
                <tr>
                    <td width="690" height="38" colspan="2">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="34" height="45">
                        <p>&nbsp;</p>
                    </td>
                    <td width="665" height="45">
                        <p><span style="font-size:14pt;">칠랑서버 곡물 10 순위</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="239" colspan="2">
                        <table cellpadding="0" height=100% cellspacing="0" align="center">
                            <tr valign=bottom>
			    $rice_list
				</tr>
			</table>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="28" colspan="2">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br><br>
<table align="center" cellpadding="0" cellspacing="0" width="700" height="350">
    <tr>
        <td width="569" height="177" background="$IMG/rankingpyo.jpg">
            <table cellpadding="0" cellspacing="0" width="700" height="350">
                <tr>
                    <td width="690" height="38" colspan="2">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="34" height="45">
                        <p>&nbsp;</p>
                    </td>
                    <td width="665" height="45">
                        <p><span style="font-size:14pt;">칠랑서버 경험치 10 순위</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="239" colspan="2">
                        <table cellpadding="0" height=100% cellspacing="0" align="center">
                            <tr valign=bottom>
			    $class_list
				</tr>
			</table>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="28" colspan="2">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br><br>
<table align="center" cellpadding="0" cellspacing="0" width="700" height="350">
    <tr>
        <td width="569" height="177" background="$IMG/rankingpyo.jpg">
            <table cellpadding="0" cellspacing="0" width="700" height="350">
                <tr>
                    <td width="690" height="38" colspan="2">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="34" height="45">
                        <p>&nbsp;</p>
                    </td>
                    <td width="665" height="45">
                        <p><span style="font-size:14pt;">칠랑서버 사살 10 순위</span></p>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="239" colspan="2">
                        <table cellpadding="0" height=100% cellspacing="0" align="center">
                            <tr valign=bottom>
			    $dead_list
				</tr>
			</table>
                    </td>
                </tr>
                <tr>
                    <td width="690" height="28" colspan="2">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
<br>
<p align="center"><form action="$FILE_TOP" method="post"><input type=submit style="font-family:궁서; color:rgb(204,255,0); background-color:rgb(153,102,0);" value="메뉴로 돌아온다."></form><br>
</td>
    </TR>
    <tr>
        <td width="1101" height="11" background="$IMG/backg.gif"><p><img src="$IMG/down.gif" width="950" height="26" border="0"></p>
</form>
</td>
    </TR>
  </TBODY>
</TABLE></body>
EOM

	&FOOTER;

	exit;
}

