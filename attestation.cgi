sub ATTESTATION {

	&HEADER;
print <<NEW;
<center>★ 메일에 첨부된 인증키와 ID와 패스워드를 입력해주십시오.<BR>
★ 인증 키가 등록되면 게임을 개시할 수가 있습니다.<p>

<center><form method=$method action=$FILE_ENTRY>
<table bgcolor=$TABLE_C><tbody bgcolor=$TD_C3>
<TR><TH bgcolor=$TD_C2 colspan=2>인증</TH></TR>
<TR><TH>ID</TH><TD>
<input type=text name=id class=text size=10></TD></TR>
<TR><TH>패스워드</TH><TD>
<input type=password name=pass class=text size=10></TD></TR>
<TR><TH>인증 키</TH><TD>
<input type=password name=key class=text size=10></TD></TR>
</TD></TR>
<input type=hidden name=mode value="SET_ENTRY">
<TR><TD bgcolor=$TD_C4 colspan=2 align=center><input type=submit value="인증"></TD></TR>
</TBODY></TABLE>
</form>

NEW
	&FOOTER;
	exit;
}

sub SET_ENTRY {

	&HOST_NAME;
	&CHARA_MAIN_OPEN;
	$akey = crypt("$kpass",wd);

	if($akey ne $in{'key'}){&ERR2("인증 키가 다릅니다.\n");}
	if(($kos & 1) eq 1){&ERR2("이미 인증이 끝난 상태입니다.");}

	&MAP_LOG("<img src=$IMG/j14.gif> $kname님이 메일인증절차를 완료하셨습니다..");
	$kos|=1;

	&CHARA_MAIN_INPUT;
	&HEADER;

	print qq|인증이 완료했습니다.<br>\n|;
	print qq|ID는 $kid입니다.<br>\n|;
	print qq|패스워드는 $kpass입니다.<br><br>\n|;

	print qq|메일인증은 이것으로 완료입니다.<br>\n|;
	print qq|메인화면에서 로그인해주시기 바랍니다..<br>\n|;

	print qq|<a href="$FILE_TOP">[돌아온다]</a>\n|;
	&FOOTER;
	exit;
}

1;