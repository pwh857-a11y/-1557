
sub GERAE{
						$ksub2=0;

						if($zsouba){
							if($kskill =~ /Ab/){
							if($cnum > 5000){
								$cnum = 5000;
							}
							}else{
							if($cnum > 3000){
							$cnum = 3000;
							}
							}

							if($kcodea =~ /C7/ && 30 > rand(100)){
								if($kchat > rand(200)){
								$kqpoint += 1;
								&K_LOG("$mmonth월 : [상인] 이게 뭔가? 백일취? 처음듣는 술인데? 한번 먹어볼까?");
								&K_LOG("$mmonth월 : 백일취가 상인들 사이에서 평이 상당히 좋은 모양이다.");
								}else{
								&K_LOG("$mmonth월 : [상인] 지금 장사하느라 바쁘니까 이런 쓸데없는 건 안가져왔으면 좋겠네.");
								}
							}

							if(!$cno){
								if($kgold >= $cnum){
									if($cnum * $zsouba){
										if($kskill =~ /Bb/){
										$kadd = int(((2-$zsouba) * $cnum)*1.5);
										}else{
										$kadd = int((2-$zsouba) * $cnum);
										}
									}else{
										$kadd = 0;
									}
									$kgold -= $cnum;
									$krice += $kadd;
									&K_LOG("$mmonth월 : [상인] : 금 $cnum를 지불해 $kadd의 쌀을 샀습니다.");
									$kint_ex++;
									$go_ex += int($kbank/5);
									$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
								}else{
									&K_LOG("$mmonth월 : [상인] : 소지금이 충분하지 않습니다.");
								}
							}else{
								if($krice > $cnum){
										if($kskill =~ /Bb/){
										$kadd = int(($cnum * $zsouba)*1.5);
										}else{
										$kadd = int($cnum * $zsouba);
										}
									$krice -= $cnum;
									$kgold += $kadd;
									&K_LOG("$mmonth월 : [상인] : $cnum의 쌀을 팔아 $kadd의 금을 샀습니다.");
									$kint_ex++;
									$go_ex += int($kbank/5);
									$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
								}else{
									&K_LOG("$mmonth월 : [상인] : 쌀이 충분하지 않습니다.");
								}
							}
						}
}
1;

