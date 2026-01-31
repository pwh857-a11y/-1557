sub YUSOU {

	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않았습니다.");}
	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");
	&TIME_DATA;

	$comlist = 66;

	$no = $in{'no'} + 1;
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	foreach(@z){
		if("$_" ne "" && $town_cou[$_] eq $kcon){
			$t_mes .= "［$town_name[$_]성］ ";
		}
	}

	$move_rice = $kleat*100;

	if( $zshiro < $move_rice ){
		$move_rice = $zshiro;
	}
	if($t_mes eq ""){&ERR("원군을 파견할 수 있는 도시가 없습니다.");}

	&HEADER;
	print <<"EOM";
<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" width="950">
    <tr>
        <td>
            <img src="$IMG/up.gif">
        </td>
    </tr>
    <tr height="600">
        <td background="$IMG/backg.gif">
<table align="center" border="1" cellspacing="0" width="752" height="492" bordercolordark="white" bordercolorlight="black">
    <tr>
        <td width="1101" height="492" background="$IMG/cola.jpg">
            <table cellpadding="0" cellspacing="0" width="752" height="488" bordercolordark="white" bordercolorlight="black">
                <tr>
                    <td width="752" height="22" colspan="8">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="11" height="467" rowspan="6">
                        <p>&nbsp;</p>
                    </td>
                    <td width="52" height="236" rowspan="4">
                        <p>&nbsp;</p>
                    </td>
                    <td width="141" height="236" rowspan="4">
                        <table cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$cou_name[$kcon]국</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$kstr1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kstrt</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$kint1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kintt</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$klea1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kleat</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kcha1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kchat</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kgold1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kgold</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$krice1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$krice</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kcex1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kcex</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$ksol1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$ksol</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kgat" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kgat</span></font></td></tr></table>
                                </td>
                            </tr>
                        </table>

                    </td>
                    <td width="25" height="236" rowspan="4">
                    </td>
                    <td width="70" height="34">
                    </td>
                    <td width="24" height="236" rowspan="4">
                  </td>
                    <td width="421" height="467" rowspan="6">
<TABLE border=0 width=100% height=80%><TR><TD>
<center>
      <TABLE bgcolor=$bg_c background="$IMG/mapbg.gif" width=96% height=5 border="0" cellspacing=0>
        <TBODY>
<TR><TH colspan= 13 bgcolor=442200><font color="white" face="돋움"><span style="font-size:9pt;">$new_date</span></font></TH></TR>

          <TR>
            <TD width=20 bgcolor=$TD_C2><font color="white" face="돋움"><span style="font-size:9pt;">-</span></font></TD>
EOM
&JIDO1;
print <<"EOM";
        </TBODY>
                                                            </tr>
      </TABLE>
<br>
$zname성으로부터 원군파견가능 지역<BR>
$t_mes
<br><br>
<b>원군을 파견하고자 하는 성의 아이콘을 클릭해주세요.</b><br>
<center>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="돌아온다">
</form></center>
</TD></TR></TABLE>
                    </td>
                    <td width="8" height="467" rowspan="6">
                    </td>
                </tr>
                <tr>
                    <td width="70" height="82">
                        <p align="center"><img src="$IMG/$kchara.gif" width="64" height="80" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="70" height="37">
                        <p align="center"><font color="white" face="돋움"><span style="font-size:9pt;">$kname</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="70" height="83">
                    </td>
                </tr>
                <tr>
                    <td width="312" height="35" colspan="5">
                    </td>
                </tr>
                <tr>
                    <td width="288" height="196" colspan="4" valign="up">
<font color="white" face="돋움"><span style="font-size:9pt;">자신의 도시의 수비병력을 다른 도시로 원군을 보냅니다.<br>자신의 원군파견가능한 거리를 숙지하신 후 자신이 있는 성 주위로 사방 8블럭안에 있는 성을 이동할 수 있습니다.<br>자신의 통솔력*100만큼의 병력을 이동시킬 수 있습니다.<br><font color=red>보내는 원군이 보낼 도시의 가용병력보다 많을 경우 원군이 되지 않습니다.</font></span></font></td>
                    <td width="24" height="196">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
        </td>
    </tr>
    <tr>
        <td>
            <img src="$IMG/down.gif">
        </td>
    </tr>
</table>
</body>
EOM

	&FOOTER;

	exit;

}





sub YUSOU12 {

	&CHARA_MAIN_OPEN;
	&CHARA_ITEM_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");
	&TIME_DATA;

	$move_rice = $kleat*100;

	if( $zshiro < $move_rice ){
		$move_rice = $zshiro;
	}

	&HEADER;
	print <<"EOM";
<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" width="950">
    <tr>
        <td>
            <img src="$IMG/up.gif">
        </td>
    </tr>
    <tr height="600">
        <td background="$IMG/backg.gif">
<table align="center" border="1" cellspacing="0" width="752" height="492" bordercolordark="white" bordercolorlight="black">
    <tr>
        <td width="1101" height="492" background="$IMG/cola.jpg">
            <table cellpadding="0" cellspacing="0" width="752" height="488" bordercolordark="white" bordercolorlight="black">
                <tr>
                    <td width="752" height="22" colspan="8">
                        <p>&nbsp;</p>
                    </td>
                </tr>
                <tr>
                    <td width="11" height="467" rowspan="6">
                        <p>&nbsp;</p>
                    </td>
                    <td width="52" height="236" rowspan="4">
                        <p>&nbsp;</p>
                    </td>
                    <td width="141" height="236" rowspan="4">
                        <table cellpadding="0" cellspacing="0">
                            <tr>
                                <td width="131" height="18">
                                    <p><font color="white"><span style="font-size:9pt;">$cou_name[$kcon]국</span></font></p>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$kstr1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kstrt</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$kint1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kintt</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
				<table cellpadding="0" cellspacing="0"><tr><td width="$klea1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kleat</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kcha1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kchat</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kgold1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kgold</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$krice1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$krice</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kcex1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kcex</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$ksol1" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$ksol</span></font></td></tr></table>
                                </td>
                            </tr>
                            <tr>
                                <td width="131" height="18">
                                <table cellpadding="0" cellspacing="0"><tr><td width="$kgat" bgcolor="#006600"><font color="white"><span style="font-size:8pt;">$kgat</span></font></td></tr></table>
                                </td>
                            </tr>
                        </table>

                    </td>
                    <td width="25" height="236" rowspan="4">
                    </td>
                    <td width="70" height="34">
                    </td>
                    <td width="24" height="236" rowspan="4">
                  </td>
                    <td width="421" height="467" rowspan="6">
<TABLE border=0 width=100% height=80%><TR><TD>
<center>
<form action="$COMMAND" method="POST"><font color="white" face="돋움">
$no_list
<BR>
<table width="300" border="0" cellpadding="2" cellspacing="1" bgcolor=$TABLE_C>
<tr bgcolor=$TD_C3>
<td width="10%"><span style="font-size:9pt;">&nbsp;</span></td>
<td width="30%" align="center"><span style="font-size:9pt;">성의 수비병</span></td>
<td width="30%" align="center"><span style="font-size:9pt;">원군파견가능</span></td>
<td><span style="font-size:9pt;">원군파견병력</span></td>
</tr>
<tr bgcolor=$TD_C3>
<td>
<p align="center"><span style="font-size:9pt;">원군</span></td>
<td><p align="center"><span style="font-size:9pt;">$zshiro명</span></td>
<td>
<p align="center"><span style="font-size:9pt;">$move_rice명</span></td>
<td align="right"><span style="font-size:9pt;"><input type=text name=rice value="0" size=6 maxlength=5 style="ime-mode:disabled;text-align:right;"></span>명</td>
</tr>
</table>
<br>
<center>
<table>
    <tr>
        <td>
<input type=hidden name=mode value=45>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=num value=$in{'num'}>
<input type=submit value="이동한다"></form>
        </td>
        <td>
<center>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="돌아온다">
</form></center>        </td>
    </tr>
</table>
                                                        </center>
                                                    </form>
                                                </center></TD></TR></TABLE>
                    </td>
                    <td width="8" height="467" rowspan="6">
                    </td>
                </tr>
                <tr>
                    <td width="70" height="82">
                        <p align="center"><img src="$IMG/$kchara.gif" width="64" height="80" border="0"></p>
                    </td>
                </tr>
                <tr>
                    <td width="70" height="37">
                        <p align="center"><font color="white" face="돋움"><span style="font-size:9pt;">$kname</span></font></p>
                    </td>
                </tr>
                <tr>
                    <td width="70" height="83">
                    </td>
                </tr>
                <tr>
                    <td width="312" height="35" colspan="5">
                    </td>
                </tr>
                <tr>
                    <td width="288" height="196" colspan="4" valign="up">
<font color="white" face="돋움"><span style="font-size:9pt;">자신의 도시의 수비병력을 다른 도시로 원군을 보냅니다.<br>자신의 원군파견가능한 거리를 숙지하신 후 자신이 있는 성 주위로 사방 8블럭안에 있는 성을 이동할 수 있습니다.<br>자신의 통솔력*100만큼의 병력을 이동시킬 수 있습니다.<br><font color=red>보내는 원군이 보낼 도시의 가용병력보다 많을 경우 원군이 되지 않습니다.</font></span></font></td>
                    <td width="24" height="196">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
        </td>
    </tr>
    <tr>
        <td>
            <img src="$IMG/down.gif">
        </td>
    </tr>
</table>
</body>
EOM

	&FOOTER;

	exit;

}







sub YUSOU2 {

	$gungold=int($in{'rice'}/20);

	if($in{'no'} eq ""){&ERR("NO:궕볺쀍궠귢궲궋귏궧귪갃");}
	if($in{'num'} eq ""){&ERR("뾃몭먩궕볺쀍궠귢궲궋귏궧귪갃");}
	if($in{'gold'} < 0 ){&ERR("뗠뾃몭쀊궕볺쀍궠귢궲궋귏궧귪갃");}
	if($in{'rice'} < 0 ){&ERR("빜쀆뾃몭쀊궕볺쀍궠귢궲궋귏궧귪갃");}
	if($in{'gold'} <= 0 && $in{'rice'} <= 0){&ERR("뾃몭쀊궕0궳궥갃");}

	if($in{'gold'} <= 0){
		$in{'gold'} = 0;
	}
	if($in{'rice'} <= 0){
		$in{'rice'} = 0;
	}

	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;
	$num = $in{'num'};
	$hit=0;


	$move_gold = $klea*200;
	$move_rice = $klea*500;

	if( $zdef_att < $move_gold ){
		$move_gold = $zdef_att;
	}
	if( $zshiro < $move_rice ){
		$move_rice = $zshiro;
	}

	if($in{'gold'} > $move_gold || $in{'rice'} > $move_rice ){&ERR("띍묈뾃몭쀊귩뎭궑궲궋귏궥갃");}

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"45<>$gungold<>$town_name[$num]성에 $in{'rice'}명의 원군[금:$gungold]<>$tt<>$in{'gold'},$in{'rice'}<>$in{'num'}<><>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);

			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"45<><>$town_name[$num]성에 $in{'rice'}명의 원군[금:$gungold]<>$tt<>$in{'gold'},$in{'rice'}<>$in{'num'}<><>\n");
					$lno = $_ + 1;
					$no .= "$lno,";
				}
			}
			if(!$ahit){
				push(@NEW_COM_DATA,"$_");
			}

			$i++;
		}

	}

	open(OUT,">./charalog/command/$kid.cgi") or &ERR('긲?귽깑귩둎궚귏궧귪궳궢궫갃');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;


	print <<"EOM";
<CENTER><hr size=0><h2>$town_name[$num]성으로 원군을 보냈습니다. [소모금액:$gungold]</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="확인"></form></CENTER>
EOM

	&FOOTER;

	exit;

}

1;
