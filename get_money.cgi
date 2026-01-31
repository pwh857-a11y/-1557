sub GET_MONEY {

	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않았습니다.");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");

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

	@tmp = map {(split /<>/)[10]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];
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
<img src="$img/sam/image/b8.gif">
</TH></TR>
<TR><TD>
<center><TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/sam/image/$kchara.gif></TD><TD>무력</TD><TH>$kstr</TH><TD>지력</TD><TH>$kint</TH><TD>통솔력</TD><TH>$klea</TH></TR>
<TR><TD>금</TD><TH>$kgold</TH><TD>쌀</TD><TH>$krice</TH><TD>공헌</TD><TH>$kcex</TH></TR>
<TR><TD>소속국</TD><TH colspan=2>$cou_name[$kcon]국</TH><TD>병사</TD><TH>$ksol</TH><TD>훈련</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<center><font color=white>다른 나라의 장수를 등용합니다.<BR>등용하는데 금 200-매력치가 필요합니다.<BR>(주의 : 밀서의 문자수는 전각 60문자 이내로 작성하십시오.)</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<center><form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<p>[등용하는 상대를 선택]<BR><select name=num>
<option value="">등용하려는 장수를 선택해주십시오.
EOM

	foreach(@COU_DATA){
		($xccid,$xcname,$xcele,$xcmark,$xcking,$xcmes,$xcsub,$xcpri)=split(/<>/);
		$cou_king[$xccid] = "$xcking";
	}

	$con_l2 = "<option value=>================================= 재야인사 =================================\n";
	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		if($eid eq $kid) { next; }
		if($econ eq $kcon) { next; }
		if($cou_name[$econ] eq ""){
			$con_l2 .= "<option value=$eid>【이름:$ename】 【무력:$estr】 【지력:$eint】 【통솔력:$elea】 【매력:$echa】 【충성도:$ebank】\n";
			next;
		}
		if($wcon ne $econ){
			$con_l .= "<option value=>================================= $cou_name[$econ]국 =================================\n";
		}
		$wcon = $econ;
		if($cou_king[$econ] eq $eid){next;}
		$con_l .= "<option value=$eid>【이름:$ename】 【무력:$estr】 【지력:$eint】 【통솔력:$elea】 【매력:$echa】 【충성도:$ebank】\n";
	}

print <<"EOM";
$con_l
$con_l2
</select>

$no_list
<BR><br><font color=red>[상대에게 보내는 등용권유문]</font><BR>
<textarea name=mes cols=38 rows=3>
</TEXTAREA>
<center><br><input type=hidden name=mode value=33>
<input type=submit value="등용한다"></form>


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