
sub BONGTOG {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN("$kcon");
	$sno = $kclass / 500;
	if($sno > 43){$sno = 43;}

	open(IN,"./charalog/per/$in{'bongid'}\.cgi") or &ERR("봉토가 없습니다.");
	@BBS_DATA = <IN>;
	close(IN);


	&HEADER;

	print <<"EOM";
<body leftmargin="0" marginwidth="0" topmargin="0" marginheight="0">
<table align="center" width="950">
    <tr>
        <td height="93">
            <img src="$IMG/up.gif">
        </td>
    </tr>
    <tr>
        <td background="$IMG/backg.gif">
<TABLE WIDTH="100%" height=100%>
<TBODY>
<STYLE>BODY {
	CURSOR: url('samnet.cur')
}
A {
	CURSOR: url('samnet.ani'); TEXT-DECORATION: none
}
</STYLE>
<TD WIDTH=95% height=5>
<table align="center" cellpadding="0" cellspacing="0" width="700" height="176" background="$IMG/bongtog.jpg">
    <tr>
        <td width="1101" background="$IMG/bongtog.jpg" height="186">
<table cellpadding="10" cellspacing="0" width="700" height="186">
                <tr>
                    <td width="259" height="165" rowspan="2" valign="bottom">
                        <div align="left">
                        <table border="3" cellspacing="0" bordercolordark="black" bordercolorlight="black">
                            <tr>
                                <td width="61">
                                    <p><img src="$IMG/$in{'bongimg'}\.gif" width="64" height="80" border="0"></p>
                                </td>
                            </tr>
                        </table>
<span style="filter:shadow(color=#BLACK,direction=135); color:FFFFFF; font-size:22px; height:1pt;">$in{'bongtown'}성 소재<br>$in{'bongname'}님의 
                        봉토게시판</span>
                        </div>
                    </td>
                    <td width="401" height="27">
                    </td>
                </tr>
                <tr>
                    <td width="401" valign="up" height="104">
                        <span style="filter:shadow(color=#333333,direction=135); color:FFFFFF; font-size:12px; height:1px;">이 곳은 $in{'bongtown'}성에 위치해있는 
                        $in{'bongname'}님의 봉토게시판입니다.<br>이 곳에 글을 남겨 $in{'bongname'}님에게 
                        안부를 남기는 용도입니다.<br>재야인사, 타국의 장수들도 
                        안부를 남길 수 있습니다.<br>글을 하나 쓸 때마다 해당 영주에게 
                        공헌치 +8이 지급됩니다.<br>단, 서로 공헌치 주고받기 식의 
                        도배가 GM들에게 발각될 시 접속차단<br>이나 영구삭제가 될 
                        수 있으니 주의해주시기 바랍니다.</span>                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
</TR></TD>
</TR><TR>
<TD height=5>
<TABLE border="0"><TBODY>
<TR>
<TD></TD>
<TD WIDTH=100% align=center>
<table>
    <tr>
        <td>
<form action="./mydata.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=bongid value=$in{'bongid'}>
<input type=hidden name=bongtown value=$in{'bongtown'}>
<input type=hidden name=bongname value=$in{'bongname'}>
<input type=hidden name=bongimg value=$in{'bongimg'}>
<input type=hidden name=mode value=BONGTOG_W>
<input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;" value="게시판에 글을 쓴다"></form>

        </td>
        <td>
<form action="$FILE_STATUS" method="post">   
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;" value="상태화면으로 돌아온다"></form>
        </td>
        <td>
<form action="./bong3.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=BONG3>
<input type=submit style="font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele]; border-width:1; border-color:black; border-style:solid;" value="봉토일람으로 돌아온다"></form>
        </td>
    </tr>
</table>
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD align=center>

<br>
</font>
EOM
	$BBS_NEXT_NUM = 20;

	if($in{'bbs_no'} eq ""){
		$bbs_no = 0;
	}else{
		$bbs_no = $in{'bbs_no'};
	}

	$s_n = 0;
	$n = 0;
	foreach(@BBS_DATA){
		($bbid,$bbtitle,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype,$bbno,$bbheap)=split(/<>/);
		if($bbtype eq "0"){
			if(!$bbheap){
				if($s_n >= $bbs_no && $s_n < $bbs_no + $BBS_NEXT_NUM){
				$bno = $s_n+1;
				$bb_id[$n] = $bbno;
				$n++;
				$c_mes[$bbno] = "<TABLE border=0 width=85% bgcolor=$ELE_C[$bbele]>

  <TBODY>
    <TR>
      <TD colspan=2 bgcolor=$ELE_BG[$bbele]><B><font size=3 color=$ELE_C[$xele]>제목 : $bbtitle</font></B></TD>
    </TR>
    <TR>
      <TD width=80 rowspan=3 valign=up align=center><img src=$IMG/$bbcharaimg.gif></TD>
      <TD>
      <TABLE border=0 width=100% bgcolor=$ELE_C[$bbele]>
        <TBODY>
          <TR>
            <TD width=600 bgcolor=$ELE_BG[$bbele]><font color=ffffff>$bbmes</TD>
          </TR>
        </TBODY>
      </TABLE>
      </TD>
    </TR>
    <TR>
      <TD><color=$ELE_BG[$bbele]><a href=\"javascript:info('$bbid')\">$bbname</a> </font></TD>
    </TR>
    <TR>
      <TD colspan=2 align=right><color=$ELE_BG[$bbele]>$bbtime</font></TD>
    </TR>

    <TR>
      <TD colspan=2 align=right>
<form action=\"./mydata.cgi\" method=\"post\">
<input type=text name=ins size=65 style=font-family:궁서; color:$ELE_C[$xele]; background-color:$ELE_BG[$xele];>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=b_no value=$bbno>
<input type=hidden name=mode value=BONGTOG_WRITE>
<input type=hidden name=bongid value=$in{'bongid'}>
<input type=hidden name=bongtown value=$in{'bongtown'}>
<input type=hidden name=bongname value=$in{'bongname'}>
<input type=hidden name=bongimg value=$in{'bongimg'}>
<input type=submit value=답신>
</TD></TR></form>";
				}
			$s_n++;
			}
		}
	}

	foreach(@BBS_DATA){
		($bbid,$bbtitle,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype,$bbno,$bbheap)=split(/<>/);
		if($bbtype eq "0"){
			if($bbheap){
				$l=0;
				foreach(@bb_id){
					if($bbheap eq $bb_id[$l]){
					$c_mes[$bbheap] .= "<TR><TD colspan=2 width=100%><TABLE cellspacing=1 width=100% bgcolor=$ELE_BG[$bbele]><TBODY bgcolor=$ELE_C[$bbele]><TR><TD width=100%><font color=$ELE_BG[$bbele]>$bbmes</TD><TD bgcolor=$ELE_BG[$bbele]><img src=$IMG/$bbcharaimg.gif></TD></TR><TR><TD colspan=2><font size=1 color=$ELE_BG[$bbele]><a href=\"javascript:info('$bbid')\">$bbname</a> <small>\[$bbtime\]</small></TD></TR></TABLE></TD></TR>";
					}
					$l++;
				}
			}
		}
	}

	$s=@c_mes;
	$d=0;
	foreach(@c_mes){
		$new_c_mes[$s] = $c_mes[$d];
		$s--;
		$d++;
	}

	foreach(@new_c_mes){
		if($_ ne ""){
			print "$_ </TBODY></TABLE><p>";
		}
	}

	$q=0;
	$n_bbs = $bbs_no + $BBS_NEXT_NUM;
	if($s_n >= $n_bbs){
	print " <form action=\"./mydata.cgi\" method=\"post\">
<input type=hidden name=mode value=BONGTOG>
<input type=hidden name=bbs_no value=$n_bbs>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=bongid value=$in{'bongid'}>
<input type=hidden name=bongtown value=$in{'bongtown'}>
<input type=hidden name=bongname value=$in{'bongname'}>
<input type=hidden name=bongimg value=$in{'bongimg'}>
<input type=submit value=\"다음의 $BBS_NEXT_NUM건\">
</form>";
	}
print <<"EOM";
</CENTER>
</TD>
</TR>
</TBODY></TABLE>
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
1;