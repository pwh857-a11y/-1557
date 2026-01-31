sub NEW_CHARA {



	open(IN,"$member_list") or &ERR2('파일을 열지 않았습니다. err no :country');
	@MEMBER_DATA = <IN>;
	close(IN);

	foreach(@MEMBER_DATA){
		($mname,$mpass)=split(/<>/);
		if($mname eq "$hi[$in{'chara'}]"){
		if($mpass eq "$in{'pass'}"){
		}else{
		&E_ERR("「$mname」이란 장수명은 특수 전용이므로 사용할 수 없습니다.");
		}
		}
	}

	&CHEACKER;
	if($CHARA_STOP){ &ERR2("현재 신규 등록은 받아들이지 않고 있습니다."); }
	if ($in{'license'} eq "") {&E_ERR("칠랑서버의 이용약관이 동의하지 않았습니다."); }
	if ($in{'id'} =~ m/[^0-9a-zA-Z]/) {&E_ERR("ID에 반격영숫자 이외의 문자가 포함되어 있습니다."); }
	if ($in{'pass'} =~ m/[^0-9a-zA-Z]/) {&E_ERR("패스워드에 반격영숫자 이외의 문자가 포함되어 있습니다."); }
	if ($in{'mail'} eq "" || $in{'mail'} !~ /(.*)\@(.*)\.(.*)/){&E_ERR("메일의 입력이 올바르지 않습니다.");}
	if($in{'id'} eq "" or length($in{'id'}) < 1 or length($in{'id'}) > 8) { &E_ERR("ID는, 1문장 이상으로 입력하길 바랍니다."); }
	elsif($in{'pass'} eq "" || length($in{'pass'}) < 1 || length($in{'pass'}) > 8) { &E_ERR("패스워드는 1문장 이상으로 입력하길 바랍니다."); }
	elsif($in{'con'} eq "") { &E_ERR("초기 위치가 선택되지 않았습니다."); }
	elsif($in{'mail'} eq "\@" || $in{'mail'} eq "") { &E_ERR("메일의 입력이 올바르지 않습니다."); }
	elsif($in{'pass'} eq "" || length($in{'pass'}) < 1 || length($in{'pass'}) > 16) { &E_ERR("캐릭터의 패스워드가 올바르게 입력되지 않았습니다."); }
	elsif($in{'id'} eq $in{'pass'}){&E_ERR("ID와 패스워드가 같은 경우, 등록할 수 없습니다."); }
	elsif($in{'type'} eq "") { &E_ERR("장수 타입이 선택되지 않았습니다."); }

	if ($in{'chara'} =~ m/[^0-9]/){&E_ERR("올바르지 않습니다."); }


	if($in{'cou_name1'} eq "1"){
		$in{'cou_name'} = "위";
		$in{'ele'} = "1";
	}elsif($in{'cou_name1'} eq "2"){
		$in{'cou_name'} = "촉";
		$in{'ele'} = "2";
	}elsif($in{'cou_name1'} eq "3"){
		$in{'cou_name'} = "오";
		$in{'ele'} = "3";
	}elsif($in{'cou_name1'} eq "4"){
		$in{'cou_name'} = "초";
		$in{'ele'} = "4";
	}elsif($in{'cou_name1'} eq "5"){
		$in{'cou_name'} = "연";
		$in{'ele'} = "5";
	}elsif($in{'cou_name1'} eq "6"){
		$in{'cou_name'} = "한";
		$in{'ele'} = "6";
	}elsif($in{'cou_name1'} eq "7"){
		$in{'cou_name'} = "고구려";
		$in{'ele'} = "7";
	}elsif($in{'cou_name1'} eq "8"){
		$in{'cou_name'} = "신라";
		$in{'ele'} = "8";
	}elsif($in{'cou_name1'} eq "9"){
		$in{'cou_name'} = "백제";
		$in{'ele'} = "9";
	}

	open(IN,"$COUNTRY_LIST") or &ERR2('파일을 열지 않았습니다. err no :country');
	@COU_DATA = <IN>;
	close(IN);

	foreach(@COU_DATA){
		($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/);
	if($xxname eq $in{'cou_name'}){&E_ERR("그 나라는 이미 존재합니다.");}
	}

	$st[0] = 10;
	$st[1] = 10;
	$st[2] = 10;
	$st[3] = 10;

	for($i=0;$i<100;$i++){
		$st[int(rand(4))]++;
	}
	for($i=0;$i<4;$i++){
		$st[int(rand(4))]+=5;
	}

	if($in{'type'} eq "1"){
		$st[int(rand(4))]+=20;
		$st[int(rand(4))]+=10;
		$st[0]+=5;
		$st[1]+=5;
		if( $st[0] > $st[2] ){
			$in{'str'} = $st[0];
			$in{'int'} = $st[2];
		}else{
			$in{'str'} = $st[2];
			$in{'int'} = $st[0];
		}
		if( $st[1] > $st[3] ){
			$in{'tou'} = $st[1];
			$in{'cha'} = $st[3];
		}else{
			$in{'tou'} = $st[3];
			$in{'cha'} = $st[1];
		}
	}elsif($in{'type'} eq "2"){
		$st[int(rand(4))]+=20;
		$st[int(rand(4))]+=10;
		$st[0]+=5;
		$st[1]+=5;
		if( $st[0] < $st[2] ){
			$in{'str'} = $st[0];
			$in{'int'} = $st[2];
		}else{
			$in{'str'} = $st[2];
			$in{'int'} = $st[0];
		}
		if( $st[1] < $st[3] ){
			$in{'tou'} = $st[1];
			$in{'cha'} = $st[3];
		}else{
			$in{'tou'} = $st[3];
			$in{'cha'} = $st[1];
		}
	}else{
		$st[int(rand(4))]+=10;
		$st[int(rand(4))]+=10;
		$st[int(rand(4))]+=10;
		$st[int(rand(4))]+=10;
		$in{'str'} = $st[0];
		$in{'int'} = $st[1];
		$in{'tou'} = $st[2];
		$in{'cha'} = $st[3];
	}
	$max = $in{'str'} + $in{'int'} + $in{'tou'} + $in{'cha'};
	if($max ne "200"){
		&E_ERR("합계의 능력이 200이 아닙니다. (합계 $max)");
	}

	open(IN,"$TOWN_LIST") or &E_ERR("지정된 파일이 열리지 않습니다.");
	@TOWN_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST") or &E_ERR('파일을 열지 않았습니다. err no :country');
	@COU_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_NO_LIST") or &E_ERR('파일을 열지 않았습니다. err no :country no');
	@COU_NO_DATA = <IN>;
	close(IN);

	$zc=0;$m_hit=0;
	
	($z2name,$z2con)=split(/<>/,$TOWN_DATA[$in{'con'}]);
	if($z2con eq "" && $in{'gunju'} eq 1){
		if($in{'ele'} eq ""){
			&E_ERR("군주의 국가 색을 선택해주세요.");
		}elsif($in{'cou_name'} eq "" || length($in{'cou_name'}) < 2 || length($in{'cou_name'}) > 8) { &E_ERR("나라의 이름이 올바르게 입력되지 않았습니다."); }
		$m_hit = 1;
		$cou_name = $in{'cou_name'};
		$new_cou_no = @COU_NO_DATA + 1;
		$hit = 1;
	}else{
		foreach(@COU_DATA){
			($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
			if($xcid eq $z2con){
				$cou_name = $xname;
				$kcon = $xcid;
				$hit = 1;
			}
		}
	}


	if($lockkey) { &F_LOCK; }

	&SET_COOKIE;
	&HOST_NAME;

	$date = time();
	$pos = 2;
	open(IN,"./charalog/main/$in{'id'}.cgi");
	@NEWCHARA = <IN>;
	close(IN);

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&E_ERR("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			push(@REGIST_VI,"@page<br>");
		}
	}
	closedir(dirlist);


	$hit=0;@new_chara=();
	($rkid,$rkpass,$rkname,$rkchara,$rkstr,$rkint,$rklea,$rkcha,$rksol,$rkgat,$rkcon,$rkgold,$rkrice,$rkcex,$rkclass,$rkarm,$rkbook,$rkbank,$rksub1,$rksub2,$rkpos,$rkmes,$rkhost,$rkdate,$rkmail,$rkos,$rkskill,$rkpoint,$rkct,$rklevel,$rkexp,$rkcodea,$rkcodeb,$rkqpoint) = split(/<>/,$NEWCHARA[0]);


	foreach(@REGIST_VI){
		($rkid,$rkpass,$rkname,$rkchara,$rkstr,$rkint,$rklea,$rkcha,$rksol,$rkgat,$rkcon,$rkgold,$rkrice,$rkcex,$rkclass,$rkarm,$rkbook,$rkbank,$rksub1,$rksub2,$rkpos,$rkmes,$rkhost,$rkdate,$rkmail,$rkos,$rkskill,$rkpoint,$rkct,$rklevel,$rkexp,$rkcodea,$rkcodeb,$rkqpoint) = split(/<>/);
		if($ACCESS){
			if($host eq $rkhost ){
				&E_ERR("한 명에 대해 한 캐릭터입니다. 혹은 같은 아이피가 이미 등록되어 있습니다.");
			}
		}
		if($rkmail eq "$in{'mail'}"){
			&E_ERR("그 메일 주소는 이미 등록되어 있습니다.");
		}
		if($rkchara eq "$in{'chara'}"){
			
			&E_ERR("이미 그 장수명은 누군가가 사용하고 있습니다.");
		}
		if($kcon eq $rkcon){
			$con_num++;
		}
	}

	if($m_hit){
		$kcon = $new_cou_no;

		$month_read = "./log_file/date_count.cgi";
		open(IN,"$month_read") or &E_ERR('파일을 열지 않았습니다.');
		@MONTH_DATA = <IN>;
		close(IN);
		($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
		$old_date = sprintf("%02d\년%02d\월", $F_YEAR+$myear, $mmonth);

		push(@COU_DATA,"$new_cou_no<>$in{'cou_name'}<>$in{'ele'}<>1<>$in{'id'}<><>$hi[$in{'chara'}]<>1<><>\n");
		open(OUT,">$COUNTRY_LIST") or &E_ERR('COUNTRY 데이터를 기입할 수 없습니다.');
		print OUT @COU_DATA;
		close(OUT);

		push(@COU_NO_DATA,"$new_cou_no<>$in{'cou_name'}<>$in{'ele'}<>1<>$in{'id'}<><><>1<><>\n");
		open(OUT,">$COUNTRY_NO_LIST") or &E_ERR('COUNTRY 데이터를 기입할 수 없습니다.');
		print OUT @COU_NO_DATA;
		close(OUT);

		&TOWN_DATA_OPEN("$in{'con'}");
		$zcon = $new_cou_no;
		&TOWN_DATA_INPUT;
		&MAP_LOG2("<img src=$IMG/j13.gif> [$old_date\] $hi[$in{'chara'}], $cou_name국을 건국하다.");
		&MAP_LOG("<img src=$IMG/j13.gif> [$old_date\] $hi[$in{'chara'}], $cou_name국을 건국하다.");

	}else{
		&MAP_LOG("<img src=$IMG/b18.gif> $hi[$in{'chara'}]님은 은둔생활을 벗어나 난세에 뛰어들었습니다.");
	}

	@NEW_COM=();
	for($i=0;$i<$MAX_COM;$i++){
		push(@NEW_COM,"<><><>$tt<><><>50<>\n");
	}

	open(OUT,">./charalog/command/$in{'id'}.cgi");
	print OUT @NEW_COM;
	close(OUT);

	@NEW_COM1=();
	for($i=0;$i<30;$i++){
		push(@NEW_COM1,"일반공격<>1<>0<>0<>\n");
	}

	open(OUT,">./charalog/command1/$in{'id'}.cgi");
	print OUT @NEW_COM1;
	close(OUT);

	@NEW_HIS=();

	open(OUT,">./charalog/history/$in{'id'}.cgi");
	print OUT @NEW_HIS;
	close(OUT);

	if($ATTESTATION){
		&mail_to;
		$os = 0;
	}else{
		$os = 1;
	}

	$ksol = 0;
	$kgat = 0;
	$kgold = 1000;
	$krice = 500;
	$kcex = 0;
	$kclass = 0;
	$karm = 0;
	$kbook = 0;
	$kbank = "16";
	$ksub1 = "";
	$ksub2 = $DEL_TURN - 10;
	$kstr = $in{'str'}+0;
	$kint = $in{'int'}+0;
	$ktou = $in{'tou'}+0;
	$kcha = $in{'cha'}+0;

	if($m_hit){
	unshift(@new_chara,"$in{'id'}<>$in{'pass'}<>$hi[$in{'chara'}]<>$in{'chara'}<>$kstr<>$kint<>$ktou<>$kcha<>$ksol<>$kgat<>$kcon<>$kgold<>$krice<>$kcex<>$kclass<>$karm<>$kbook<>$kbank<>$ksub1<>$ksub2<>$in{'con'}<>$in{'mes'}<>$host<>$date<>$in{'mail'}<>1<><>0<>$in{'con'}<>1<>0<><>A0<>0<>\n");
	}else{
	unshift(@new_chara,"$in{'id'}<>$in{'pass'}<>$hi[$in{'chara'}]<>$in{'chara'}<>$kstr<>$kint<>$ktou<>$kcha<>$ksol<>$kgat<><>$kgold<>$krice<>$kcex<>$kclass<>$karm<>$kbook<>$kbank<>$ksub1<>$ksub2<>$in{'con'}<>$in{'mes'}<>$host<>$date<>$in{'mail'}<>1<><>0<>$in{'con'}<>1<>0<><>A0<>0<>\n");
	}
	open(OUT,">./charalog/main/$in{'id'}.cgi");
	print OUT @new_chara;
	close(OUT);



	if (-d $lockfile) { &UNLOCK_FILE; }
	&DATA_SEND;
	exit;
}

sub mail_to {
	$sendmail = '/usr/lib/sendmail';

	$mail_sub = "삼국지 모의전투 NET 등록 통지";
	&TIME_DATA;

	$a_pass = crypt("$in{'pass'}", wd);

	$mail_msg = <<"EOM";
안녕하십니까? $hi[$in{'chara'}] 님

$GAME_TITLE 의 세계에 오신걸 환영합니다.
등록 내용은 아래와 같으므로 필시 확인해주십시오.


★ 등록일시 : $daytime
★ 호스트명 : $host
★ 참가자명 : $hi[$in{'chara'}]
★ 이메일 : $in{'mail'}
★ 아이디 : $in{'id'}
★ 비밀번호 : $in{'pass'}
★ 인증키 : $a_pass

인증 키에 등록해야지만 게임에 참가할 수 있습니다.

[인증키 등록하러 가기]
$SANGOKU_URL/entry.cgi?mode=ATTESTATION
(☆ 이쪽으로부터 등록할 수 있습니다.)

그리고 자주 게시판을 확인하여 운영자의 공지사항을 자주보는 습관을 기릅시다.
또, 패스워드 아이디등은 재발행이 되지 않으므로 소중히 보관해주십시오.

아이디는 한 사람당 하나밖에 못만듭니다.
지속적인 자체적인 아이피검사와 whois와 해커즈랩를 이용한 검사도 하고 있습니다.
괜한 짓은 하지 않는게 좋을듯 싶습니다.
만약 적발되면 본케는 물론 나머지 아이디까지 전부 삭제하니 유의해주세요.

$GAME_TITLE운영자 김진섭

홈페이지   : http://sam-net.wo.to
EOM

	$mail_msg =~ s/<br>/\n/ig;

	open(MAIL,"| $sendmail -t") || &E_ERR("메일 송신에 실패했습니다.");
	print MAIL "To: $in{'mail'}\n";
	print MAIL "Subject: $mail_sub\n";
	print MAIL "MIME-Version: 1.0\n";
	print MAIL "Content-type: text/plain; charset=euc-kr\n";
	print MAIL "Content-Transfer-Encoding: 8bit\n";
	print MAIL "X-Mailer: $ver\n\n";
	print MAIL "$mail_msg\n";
	close(MAIL);

}

sub E_ERR {

	&HEADER;
	if (-e $lockfile) { unlink($lockfile); }
	print "<center><hr size=0><h3>ERROR !</h3>\n";
	print "<P><font color=red><B>$_[0]</B></font>\n";
print "<form action=\"$FILE_ENTRY\" method=\"post\"><input type=hidden name=id value=$in{'id'}><input type=hidden name=pass value=$in{'pass'}><input type=hidden name=mail value=$in{'mail'}><input type=hidden name=url value=$in{'url'}><input type=hidden name=chara_name value=$hi[$in{'chara'}]><input type=hidden name=mes value=$in{'mes'}><input type=hidden name=mode value=entry><input type=submit value=\"돌아온다\"></form>";
	print "<P><hr size=0></center>\n</body></html>\n";
	exit;
}

sub CHEACKER {

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);


	$num = @CL_DATA;

	if($ENTRY_MAX){
		if($num > $ENTRY_MAX){
			&ERR2("최대 등록수 \[$ENTRY_MAX\]를 넘고 있습니다. 현재 신규 등록을 할 수 없습니다.");
		}
	}
}

1;