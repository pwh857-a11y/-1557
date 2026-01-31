sub BONGTOG_WRITE{

	&CHARA_MAIN_OPEN;
	&TIME_DATA;
	&HOST_NAME;
	&COUNTRY_DATA_OPEN("$kcon");
	&TOWN_DATA_OPEN($kpos);
	if(length($in{'title'}) > 40 || length($in{'ins'}) > 1000) { &ERR("좀 더 간략하게 글을 써주세요"); }

	if(($in{'title'} eq "" && $in{'b_no'} eq "")|| $in{'ins'} eq "") { &ERR("메세지가 입력되있지 않습니다"); }

	if($lockkey) { &F_LOCK; }
	open(IN,"./charalog/per/$in{'bongid'}\.cgi") or &ERR2('봉토가 없습니다.');
	@BBS_DATA1 = <IN>;
	close(IN);

	&GWAN1;

	$bbs_num = @BBS_DATA1;
	if($bbs_num > $MES_MAX) { pop(@BBS_DATA1); }

	$bbname = "<B><font size=2><a href=\"javascript:info('$kid')\">《$kname》</a></B>ID:$kid <font size=2>레벨:「Lv.$klevel」 소속국:「$xname국」<img src=$IMG/$rank_mes\.jpg>";
	if($in{"type"} eq "all"){$bbtype = 1;$back = "BONGTOG_ALL_TALK"}else{$bbtype = 0;$back = "BONGTOG"}

	($lbbid,$lbbtitle,$lbbmes,$lbbcharaimg,$lbbname,$lbbhost,$lbbtime,$lbbele,$lbbcon,$lbbtype,$lbbno,$lbbheap)=split(/<>/,$BBS_DATA1[0]);

	$bno = $lbbno + 1;

	if($in{'b_no'} ne ""){
		$b_heap = $in{'b_no'};
	}else{
		$b_heap = 0;
	}

	opendir(dirlist,"./charalog/main");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"./charalog/main/$file")){
				&ERR2("파일 오픈 에러!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	foreach(@CL_DATA){
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/);
		($estr_ex,$eint_ex,$elea_ex,$echa_ex,$esub1_ex,$esub2_ex) = split(/,/,$esub1);
			if($kid ne $eid){
			if($eid eq "$zbong1"){
				$ecex += 8;
			}elsif($eid eq "$zbong2"){
				$ecex += 8;
			}elsif($eid eq "$zbong3"){
				$ecex += 8;
			}
			&ENEMY_INPUT;
		}
	}
			
	unshift(@BBS_DATA1,"$kid<>$in{'title'}<>$in{'ins'}<>$kchara<>$bbname<>$host<>$daytime<>$xele<>$kcon<>$bbtype<>$bno<>$b_heap<>\n");

	

	open(OUT,">./charalog/per/$in{'bongid'}\.cgi") or &ERR('봉토가 없습니다.');
	print OUT @BBS_DATA1;
	close(OUT);

	if (-e $lockfile) { unlink($lockfile); }


	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2>$in{'bongname'}님의 봉토게시판에 글을 올렸습니다.</h2><p>

<form action="./mydata.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=$back>
<input type=hidden name=bongid value=$in{'bongid'}>
<input type=hidden name=bongtown value=$in{'bongtown'}>
<input type=hidden name=bongname value=$in{'bongname'}>
<input type=hidden name=bongimg value=$in{'bongimg'}>
<input type=submit value="확인"></form></CENTER>
EOM
	&FOOTER;
	exit;
	
}
1;