sub TANREN {

	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않았습니다.");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;

	&HEADER;
	$no = $in{'no'} + 1;

	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}
	$get_sol = $klea - $ksol;
	print <<"EOM";
<TABLE border=0 width=100% height=80%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH>
<img src="$IMG/b10.gif">
</TH></TR>
<TR><TD>

<center><TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>무력</TD><TH>$kstr</TH><TD>지력</TD><TH>$kint</TH><TD>통솔력</TD><TH>$klea</TH></TR>
<TR><TD>금</TD><TH>$kgold</TH><TD>쌀</TD><TH>$krice</TH><TD>공헌</TD><TH>$kcex</TH></TR>
<TR><TD>소속국</TD><TH colspan=2>$cou_name[$kcon]국</TH><TD>병사</TD><TH>$ksol</TH><TD>훈련</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<center><font color=white>수련을 쌓는 것으로 경험이 오릅니다.<BR>수련은 무료입니다.<BR>경험치가 10 포인트를 넘으면 능력치가 상승합니다.<br><b>단, 올리고자 하는 능력치가 90 이상이 되어야지만 수련을 할 수 있습니다.</b></font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<center>어느 능력을 수련합니까?
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<select name=num>
<option value=1>무력
<option value=2>지력
<option value=3>통솔력
<option value=4>매력
</select>
$no_list
<input type=hidden name=mode value=27>
<input type=submit value="수련한다"></form>


<center><form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="돌아온다"></form></CENTER>
</TD></TR></TABLE>
</TD></TR></TABLE>

EOM

	&FOOTER;

	exit;

}
1;