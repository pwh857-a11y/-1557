sub entry_can{
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");
	&CHARA_ITEM_OPEN;
	&TIME_DATA;

	if(!$wday){&error("대회 개최일에 등록 해제할 수 없습니다.");}
	
	open(IN,"./data/entry_list.cgi") or &ERR2("등록자 리스트가 열리지 않습니다.");
	@ENTRY_DATA = <IN>;
	close(IN);
	@N_ENTRY=();
	foreach(@ENTRY_DATA){
		($e_id,$e_name,$e_chara,$e_con,$e_cname,$e_cele,$e_point,$e_flg)=split(/<>/);
		if($e_id eq $kid){$ehit=1;}
		else{push(@N_ENTRY,"$_");}
	}
	if(!$ehit){&ERR2("등록되어 있지 않습니다.");}
	open(OUT,">./data/entry_list.cgi");
	print OUT @N_ENTRY;
	close(OUT);

	&HEADER;
	
	print <<"EOF";
<TABLE border="0" width="80%" bgcolor="#ffffff" height="150" align=center CLASS=FC>
  <TBODY>
    <TR>
      <TD colspan="2" align="center" bgcolor="#993300"><FONT color="#ffffcc">등록 해제</FONT></TD>
    </TR>
    <TR>
      <TD bgcolor="#ffffcc" width=20% align=center><img src="./img/etc/arena.jpg"></TD>
      <TD bgcolor="#330000"><FONT color="#ffffcc">등록을 해제했습니다.</FONT></TD>
    </TR>
    <TR>
      <TD colspan="2" align="right">
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="돌아온다"></form></TD>
	
    </TR>
  </TBODY>
</TABLE>
EOF
	&footer;
	exit;
}
1;
