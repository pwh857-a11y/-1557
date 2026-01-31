
sub HWAGAE{
				$ksub2=0;
				if($kgold<300){
					&K_LOG("$mmonth월 : 자금부족으로 실행할 수 없었습니다.");
				}elsif($zsub1<500){
					&K_LOG("$mmonth월 : 화계를 설치하기에는 기술력이 충분하지 않습니다.");
				}else{
					open(IN,"$TRAP_LIST");
					@TRAP_DATA = <IN>;
					close(IN);
					$kgold -= 300;
					$trap_count = 0;
					$trap_flg = 0;
					$trapmax = @TRAP_DATA;
					if($kskill =~ /Dc/){
					$r = int(rand($kintt) + rand($kintt));
					}else{
					$r = int((rand($kintt) + rand($kintt))/2);
					}
					for($trapi=0;$trapi<$trapmax;$trapi++){
						($tid,$tname,$ttown_id,$tcon,$ttrap,$tint) = split(/<>/,$TRAP_DATA[$trapi]);
						if( $ttown_id == $kpos && $ttrap == 1 && $tid eq $kid ){
							$r += 5;
							if($r > $tint){
								$trap_flg = 1;
							}else{
								$trap_flg = -1;
							}
							last;
						}elsif( $ttown_id == $kpos ){
							$trap_count++;
						}
					}
					if( $trap_flg == -1 ){
						&K_LOG("$mmonth월 : 화계를 개량할 수 없었습니다.");
					}elsif( $trap_flg == 1 ){
						splice(@TRAP_DATA,$trapi,1,"$kid<>$kname<>$kpos<>$kcon<>1<>$r<>\n");
					if($kskill =~ /Dc/){
						$kcex += 40;
						$kexp += 40;
						$kpoint += 16;
					}else{
						$kcex += 20;
						$kexp += 20;
						$kpoint += 8;
					}
						&K_LOG("$mmonth월 : $zname성의 화계를 개량하였습니다.");
						$kint_ex += 2;
						$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					}elsif( $trap_count < 5 ){
						push(@TRAP_DATA,"$kid<>$kname<>$kpos<>$kcon<>1<>$r<>\n");
					if($kskill =~ /Dc/){
						$kcex += 40;
						$kexp += 40;
						$kpoint += 16;
					}else{
						$kcex += 20;
						$kexp += 20;
						$kpoint += 8;
					}
						$kqpoint = 1 if $kcodea =~ /D1/;
						&K_LOG("$mmonth월 : $zname성에 화계를 설치하였습니다.");
						$kint_ex += 2;
						$go_ex += int($kbank/5);
						$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					}else{
						&K_LOG("$mmonth월 : 이미 $zname성에서는 5개의 함정이 설치되었습니다.");
					}
				}
}
1;

