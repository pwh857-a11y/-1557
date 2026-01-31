
sub HUNRYEON{
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

						$ksub2=0;

						if($kskill =~ /Ea/){
						$kgat += int(($kleat)/2 + rand($kleat/5));
						}else{
						$kgat += int(($kleat)/4 + rand($kleat/5));
						}

						if($kskill =~ /Ga/){
							if($kgat > 120){
								$kgat = 120;
							}
						}else{
							if($kgat > 100){
								$kgat = 100;
							}
						}


						&K_LOG("$mmonth월 : 병사의 훈련도가 <font color=red>$kgat</font>가 되었습니다.");
						$klea_ex++;
						$go_ex += int($kbank/5);

						$kcex += 15;
						$kexp += 15;
						$kpoint += 4;



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
						}
						$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
}
1;

