sub DATA_SEND {

	open(IN,"$TOWN_LIST") or &ERR2("지정된 파일이 열리지 않습니다.");
	@TOWN = <IN>;
	close(IN);

	&CHARA_MAIN_OPEN;
	&HEADER;

	print <<"EOM";
<CENTER><h3>-- 등록 완료 --</h3>
<hr size=0>
$kname로 $GAME_TITLE의 세계에 등록되었습니다.<BR>아이디와 비밀번호는 잊지 않게 메모해두시거나 기억하시길 바랍니다.
<hr size=0>
ID : <font color=red>$in{'id'}</font><BR>
PASS : <font color=red>$in{'pass'}</font><BR>
<p>
스테이터스<BR><table border=0 bgcolor=$TABLE_C cellspacing=1><TBODY bgcolor=$TD_C4>
<tr><td rowspan="8" align="center"><img src="$IMG/$in{'chara'}.gif"></td>
<td class="b1">이름</td><td width=50>$hi[$in{'chara'}]</td>
<td class="b1">나라</td><td>$cou_name</td></tr>
<tr><td class="b1">계급</td><td>$LANK[0]</td>
<td class="b1">초기위치</td><td>$z2name</td></tr>
<tr><td class="b1">무력</td><td width=50>$in{'str'}</td>
<td class="b1">지력</td><td>$in{'int'}</td></tr>
<tr><td>통솔력</td><td>$in{'tou'}</td>
<td>매력</td><td>$in{'cha'}</td></tr>
</table><p>
<form action="$FILE_ENTRY" method="post">
<input type="hidden" name=mode value=RESISDENTS>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=num value="0">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="게임의 설명">
</form><p>
<form action="$FILE_STATUS" method="post">
<input type="hidden" name=mode value=STATUS>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="게임을 개시">
</form><p>

</form>
<form action="$FILE_ENTRY" method="post" name=para>
<input type="hidden" name="mode" value="ENTRY2">
<input type="hidden" name="mail" value="$in{'mail'}">
<input type="hidden" name="id" value="$in{'id'}">
<input type="hidden" name="pass" value="$in{'pass'}">
<input type="hidden" name="chara_name" value="$in{'chara_name'}">
<input type="hidden" name="chara" value="$in{'chara'}">
<input type="hidden" name="type" value="$in{'type'}">
<td align="center">
</CENTER>
EOM

		&FOOTER;

		exit;
}
1;