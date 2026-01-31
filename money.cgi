sub MONEY {

	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않았습니다.");}
	&CHARA_MAIN_OPEN;

	&TIME_DATA;
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	&HEADER;
	$no = $in{'no'} + 1;


	$get_sol = $klea - $ksol;
	print <<"EOM";
<TABLE border=0 width=100% height=80%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH>
<img src="$IMG/b12.gif">
</TH></TR>
EOM
	if("$ENV{'HTTP_REFERER'}" eq "$SANGOKU_URL/status.cgi"){ 

print <<"EOM";

<TR><TD>
<center><TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>무력</TD><TH>$kstr</TH><TD>지력</TD><TH>$kint</TH><TD>통솔력</TD><TH>$klea</TH></TR>
<TR><TD>금</TD><TH>$kgold</TH><TD>쌀</TD><TH>$krice</TH><TD>공헌</TD><TH>$kcex</TH></TR>
<TR><TD>소속국</TD><TH colspan=2>$cou_name[$kcon]국</TH><TD>병사</TD><TH>$ksol</TH><TD>훈련</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
EOM
	}
print <<"EOM";

<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<center><font color=white>다른 도시로 이동합니다.<BR></font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<center>어디로 이동하시겠습니까?
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<select name=num>
EOM

	$xx=0;
	foreach(@town_name){
		if($xx < 53){
		print "<option value=$xx>$town_name[$xx]";
		}else{}
		$xx++;
	}

	foreach(@z){
		if("$_" ne ""){
			$move_list .= "$town_name[$_]<BR>";
		}
	}
print <<"EOM";
</select>


<p><font color=red>[$zname로부터 이동가능인 거리]</font><br><BR>$move_list
$no_list
<br>
<center><input type=hidden name=mode value=20>
<input type=submit value="이동한다"></form>


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