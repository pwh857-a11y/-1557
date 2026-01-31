sub GET_SOL2 {

	if($in{'no'} eq ""){&ERR("NO:가 입력되지 않았습니다.");}
	if($in{'num'} eq ""){&ERR("징병하는 인원수가 입력되지 않았습니다.");}
	if($in{'type'} eq ""){&ERR("징병하는 종류가 입력되지 않았습니다.");}
	if($in{'num'} =~ m/[^0-9]/){&ERR("징병하는 인원수에 숫자 이외의 문자가 포함되어 있습니다."); }
	&CHARA_MAIN_OPEN;
	&TIME_DATA;

	# --- v19 region restriction for special troops (added; no deletions) ---
	my ($__tx,$__ty)=(-1,-1);
	my $__pos_idx = $kpos;
	if($__pos_idx ne "" && $__pos_idx =~ /^\d+$/){
		open(__TIN,"$F_TOWN_LIST");
		my @__TD=<__TIN>;
		close(__TIN);
		if($__pos_idx <= $#__TD){
			my @__F=split(/<>/, $__TD[$__pos_idx]);
			$__tx=$__F[10]; $__ty=$__F[11];
		}
	}
	my $__region="";
	if($__tx ne "" && $__ty ne "" && $__tx >= 0 && $__ty >= 0){
		# rough regions by map coordinate
		if($__tx >= 9){ $__region="korea"; }
		elsif($__ty >= 8 && $__tx <= 4){ $__region="nanman"; }
		elsif($__tx >= 7 && $__ty <= 3){ $__region="liaodong"; }
		else{ $__region="central"; }
	}
	# restrictions: Hwarang(11)=korea only, Elephant(8)=nanman only, Shingwi(5)=liaodong only, Siege(12,17)=central only
	if($__region ne ""){
		my $__t = int($in{'type'});
		if($__t == 11 && $__region ne "korea"){ &ERR("화랑 전용 병종은 한반도 영역에서만 고용 가능합니다."); }
		if($__t == 8 && $__region ne "nanman"){ &ERR("코끼리병 전용 병종은 남만 영역에서만 고용 가능합니다."); }
		if($__t == 5 && $__region ne "liaodong"){ &ERR("신귀병 전용 병종은 요동 영역에서만 고용 가능합니다."); }
		if(($__t == 12 || $__t == 17) && $__region ne "central"){ &ERR("발석거/투석차 계열은 중원 영역에서만 고용 가능합니다."); }
	}


	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($kcha > 75){
	$ga = int($kcha/5);
	}
	$ggyo = int($in{'num'} * ($SOL_PRICE[$in{'type'}] - $ga)/30);
	if($ggyo < 10){$ggyo=int(($cnum * 10)/30);}

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"10<><>$SOL_TYPE[$in{'type'}]징병($in{'num'}명 금액:$ggyo)<>$tt<>$in{'type'}<>$in{'num'}<>$in{'gat'}<>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
					push(@NEW_COM_DATA,"10<><>$SOL_TYPE[$in{'type'}]징병($in{'num'}명 금액:$ggyo)<>$tt<>$in{'type'}<>$in{'num'}<>$in{'gat'}<>\n");
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

	open(OUT,">./charalog/command/$kid.cgi") or &ERR('파일을 열지 않았습니다.');
	print OUT @NEW_COM_DATA;
	close(OUT);
	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>NO:$no에 $mes$SOL_TYPE[$in{'type'}]($in{'num'}명) 징병을 입력했습니다. 금액:$ggyo</h2><p>
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