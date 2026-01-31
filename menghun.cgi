
sub MENGHUN{
						$ksub2=0;

						if($ksol <= 0){
							&K_LOG("$mmonth월 : 병력이 없습니다.");
							$ksol = 0;
						}elsif($krice<500){
						&K_LOG("$mmonth월 : 자금부족으로 실행할 수 없었습니다.");
						}elsif($kskill =~ /Ga/){
							if($kgat >= 120){
							&K_LOG("$mmonth월 : 병사의 훈련도가 최고치입니다.");
							$kgat = 120;
							}else{
								$z_hit = 1;
							}
						}else{
							if($kgat >= 100){
							&K_LOG("$mmonth월 : 병사의 훈련도가 최고치입니다.");
							$kgat = 120;
							}else{
								$z_hit = 1;
							}
						}


						if($z_hit){

						if($kskill =~ /Ea/){
						$kgatadd = int($kleat+40);
						}else{
						$kgatadd = int($kleat+20);
						}
						$kgat += $kgatadd;

						if($kskill =~ /Ga/){
							if($kgat > 120){
								$kgat = 120;
							}
						}else{
							if($kgat > 100){
								$kgat = 100;
							}
						}

						$krice -= 500;

						$kcex += 25;
						$kexp += 25;
						$kpoint += 8;




							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /훈련/){
										if($qup =~ /훈련/){
										$kqpoint += $kgatadd;
										}else{
										$kqpoint += $qup;
										}
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth월 : $qtalkd");
										}

									}	
								}
							}

						&K_LOG("$mmonth월 : 병사의 훈련도가 <font color=red>$kgat</font>가 되었습니다.");
						$klea_ex++;
						$kstr_ex++;
						$go_ex += int($kbank/5);
						$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";

						}
}
1;

