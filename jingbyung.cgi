
sub JINGBYUNG{
						$ksub2=0;

						if($kcha > 75){
						$ga = int($kchat/5);
						}
						if($kgold < $ggyo){
							&K_LOG("$mmonth월 : [군사] : 소지금이 충분하지 않습니다.");

						}elsif($znum < $cnum){
							&K_LOG("$mmonth월 : [군사] : 농민들이 충분하지 않습니다.");
						}elsif($cnum <= 0){
							&K_LOG("$mmonth월 : [군사] : 병사를 0명 이하로 징병할 수 없습니다.");
						}elsif($zpri < int($cnum / 300)){
							&K_LOG("$mmonth월 ; [군사] : 농민들이 거부했습니다.");
						}elsif($znum < 0){
							&K_LOG("$mmonth월 ; [군사] : 농민들이 0 이하로 내려갈 수 없습니다.");
							$znum = 0;
						}elsif($kskill =~ /Ac/){

						if($ggyo < 10){$ggyo=int(($cnum * 10)/30);}
							if($ksub1_ex == $csub){
								if($ksol + $cnum > ($kleat)*30){
									$cnum = int(($kleat)*30) - $ksol;
								}
								$ksol += $cnum;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
							}else{
								if($cnum > ($kleat)*30){
									$cnum = $kleat*30;
								}
								$ksol = $cnum;
							}
							$kgat -= int($cnum/30);
							if($kgat < 0 ){
								$kgat = 0;
							}
							$ksub1_ex = $csub;
							$kcex += 10;
							$kexp += 10;
							$kpoint += 4;

						if($kskill =~ /Bc/ && $csub == 7){
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/60);
						}elsif($kskill =~ /Cc/ && $csub == 12){
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/40);
						}else{
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/30);
						}



							$kgold -= $ggyo;




							if($kskill =~ /Db/ && $zpri >= 75){
							}else{
							$znum -= $cnum;
							}

							$zpri -= int($cnum / 300);
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
							}

							&K_LOG("$mmonth월 : $SOL_TYPE[$ksub1_ex]를 <font color=red>+$cnum</font> 징병했습니다. [징병금액 : $ggyo]");
							if($cnum > 14){
							$kstr_ex++;
							$go_ex += int($kbank/5);
							}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}elsif("7" eq $csub && $zsub1 < 1150){
							&K_LOG("$mmonth월 : [군사] : 황실근위병을 생산하기에는 기술력이 부족합니다.");
						}elsif("15" eq $csub && $zsub1 < 899){
							&K_LOG("$mmonth월 : [군사] : 산월병을 생산하기에는 기술력이 부족합니다.");
						}elsif("8" eq $csub && $zsub1 < 750){
							&K_LOG("$mmonth월 : [군사] : 코끼리병을 생산하기에는 기술력이 부족합니다.");
						}elsif("9" eq $csub && $zsub1 < 1150){
							&K_LOG("$mmonth월 : [군사] : 산악병을 생산하기에는 기술력이 부족합니다.");
						}elsif("10" eq $csub && $zsub1 < 1100){
							&K_LOG("$mmonth월 : [군사] : 철기병을 생산하기에는 기술력이 부족합니다.");
						}elsif("11" eq $csub && $zsub1 < 1100){
							&K_LOG("$mmonth월 : [군사] : 화랑을 생산하기에는 기술력이 부족합니다.");
						}elsif("1" eq $csub && $zsub1 < 100){
							&K_LOG("$mmonth월 : [군사] : 궁병을 생산하기에는 기술력이 부족합니다.");
						}elsif("2" eq $csub && $zsub1 < 250){
							&K_LOG("$mmonth월 : [군사] : 창병을 생산하기에는 기술력이 부족합니다.");
						}elsif("3" eq $csub && $zsub1 < 450){
							&K_LOG("$mmonth월 : [군사] : 중장보병을 생산하기에는 기술력이 부족합니다.");
						}elsif("4" eq $csub && $zsub1 < 750){
							&K_LOG("$mmonth월 : [군사] : 기병을 생산하기에는 기술력이 부족합니다.");
						}elsif("6" eq $csub && $zsub1 < 800){
							&K_LOG("$mmonth월 : [군사] : 의병을 생산하기에는 기술력이 부족합니다.");
						}elsif("7" eq $csub && ($zname eq "서량" || $zname eq "무도" || $zname eq "건녕" || $zname eq "안정" || $zname eq "한중" || $zname eq "검각" || $zname eq "자동" || $zname eq "강주" || $zname eq "영안" || $zname eq "홍농" || $zname eq "완" || $zname eq "강릉" || $zname eq "무릉" || $zname eq "영릉" || $zname eq "신야" || $zname eq "강하" || $zname eq "장사" || $zname eq "계양" || $zname eq "남해" || $zname eq "진유" || $zname eq "여남" || $zname eq "시상" || $zname eq "평원" || $zname eq "복양" || $zname eq "초" || $zname eq "수춘" || $zname eq "단양" || $zname eq "여강" || $zname eq "계" || $zname eq "남피" || $zname eq "소패" || $zname eq "북평" || $zname eq "북해" || $zname eq "하비" || $zname eq "광릉" || $zname eq "오" || $zname eq "회계" || $zname eq "양평" || $zname eq "국내" || $zname eq "사비" || $zname eq "매소" || $zname eq "서라벌" || $zname eq "운남" || $zname eq "천수" || $zname eq "졸본")){
							&K_LOG("$mmonth월 : [군사] : 해당 지역에서는 황실근위병을 뽑을 수가 없습니다..");
						}elsif("5" eq $csub && $zsub1 < 1000){
							&K_LOG("$mmonth월 : [군사] : 신귀병을 생산하기에는 기술력이 부족합니다.");
						}elsif("8" eq $csub && ($zname eq "성도" || $zname eq "장안" || $zname eq "양양" || $zname eq "낙양" || $zname eq "업" || $zname eq "허창" || $zname eq "건업" || $zname eq "한" || $zname eq "무도" || $zname eq "건녕" || $zname eq "자동" || $zname eq "강주" || $zname eq "영안" || $zname eq "홍농" || $zname eq "완" || $zname eq "강릉" || $zname eq "무릉" || $zname eq "영릉" || $zname eq "신야" || $zname eq "강하" || $zname eq "장사" || $zname eq "계양" || $zname eq "남해" || $zname eq "진유" || $zname eq "여남" || $zname eq "시상" || $zname eq "평원" || $zname eq "복양" || $zname eq "초" || $zname eq "수춘" || $zname eq "단양" || $zname eq "여강" || $zname eq "계" || $zname eq "남피" || $zname eq "소패" || $zname eq "북평" || $zname eq "북해" || $zname eq "하비" || $zname eq "광릉" || $zname eq "오" || $zname eq "회계" || $zname eq "양평" || $zname eq "국내" || $zname eq "사비" || $zname eq "매소" || $zname eq "서라벌" || $zname eq "천수" || $zname eq "졸본")){
							&K_LOG("$mmonth월 : [군사] : 해당 지역에서는 코끼리병을 뽑을 수가 없습니다..");
						}elsif("9" eq $csub && ($zname eq "장안" || $zname eq "양양" || $zname eq "낙양" || $zname eq "업" || $zname eq "허창" || $zname eq "건업" || $zname eq "한" || $zname eq "홍농" || $zname eq "완" || $zname eq "강릉" || $zname eq "무릉" || $zname eq "영릉" || $zname eq "신야" || $zname eq "강하" || $zname eq "장사" || $zname eq "계양" || $zname eq "남해" || $zname eq "진유" || $zname eq "여남" || $zname eq "시상" || $zname eq "평원" || $zname eq "복양" || $zname eq "초" || $zname eq "수춘" || $zname eq "단양" || $zname eq "여강" || $zname eq "남피" || $zname eq "소패" || $zname eq "북해" || $zname eq "하비" || $zname eq "광릉" || $zname eq "오" || $zname eq "회계" || $zname eq "사비" || $zname eq "매소" || $zname eq "천수" || $zname eq "운남")){
							&K_LOG("$mmonth월 : [군사] : 해당 지역에서는 산악병을 뽑을 수가 없습니다..");
						}elsif("10" eq $csub && ($zname eq "장안" || $zname eq "양양" || $zname eq "낙양" || $zname eq "업" || $zname eq "허창" || $zname eq "건업" || $zname eq "한" || $zname eq "홍농" || $zname eq "완" || $zname eq "강릉" || $zname eq "무릉" || $zname eq "영릉" || $zname eq "신야" || $zname eq "강하" || $zname eq "장사" || $zname eq "계양" || $zname eq "남해" || $zname eq "진유" || $zname eq "여남" || $zname eq "시상" || $zname eq "평원" || $zname eq "복양" || $zname eq "초" || $zname eq "수춘" || $zname eq "단양" || $zname eq "여강" || $zname eq "남피" || $zname eq "소패" || $zname eq "북해" || $zname eq "하비" || $zname eq "광릉" || $zname eq "오" || $zname eq "회계" || $zname eq "사비" || $zname eq "매소" || $zname eq "천수" || $zname eq "운남" || $zname eq "졸본")){
							&K_LOG("$mmonth월 : [군사] : 해당 지역에서는 철기병을 뽑을 수가 없습니다..");
						}elsif("11" eq $csub && ($zname eq "성도" || $zname eq "장안" || $zname eq "양양" || $zname eq "낙양" || $zname eq "업" || $zname eq "허창" || $zname eq "건업" || $zname eq "한" || $zname eq "무도" || $zname eq "건녕" || $zname eq "안정" || $zname eq "한중" || $zname eq "검각" || $zname eq "자동" || $zname eq "강주" || $zname eq "영안" || $zname eq "홍농" || $zname eq "완" || $zname eq "강릉" || $zname eq "무릉" || $zname eq "영릉" || $zname eq "신야" || $zname eq "강하" || $zname eq "장사" || $zname eq "계양" || $zname eq "남해" || $zname eq "진유" || $zname eq "여남" || $zname eq "시상" || $zname eq "평원" || $zname eq "복양" || $zname eq "초" || $zname eq "수춘" || $zname eq "단양" || $zname eq "여강" || $zname eq "계" || $zname eq "남피" || $zname eq "소패" || $zname eq "북평" || $zname eq "북해" || $zname eq "하비" || $zname eq "광릉" || $zname eq "오" || $zname eq "회계" || $zname eq "양평" || $zname eq "국내" || $zname eq "사비" || $zname eq "매소" || $zname eq "운남" || $zname eq "천수" || $zname eq "졸본")){
							&K_LOG("$mmonth월 : [군사] : 해당 지역에서는 화랑을 뽑을 수가 없습니다..");
						}elsif("13" eq $csub && $zsub1 < 900){
							&K_LOG("$mmonth월 ; [군사] : 황건적을 생산하기에는 기술력이 부족합니다.");
						}elsif("12" eq $csub && $zsub1 < 1199){
							&K_LOG("$mmonth월 ; [군사] : 발석거를 생산하기에는 기술력이 부족합니다.");
						}elsif("17" eq $csub && $zsub1 < 1199){
							&K_LOG("$mmonth월 ; [군사] : 파쇄차를 생산하기에는 기술력이 부족합니다.");
						}elsif("15" eq $csub && ($zname eq "성도" || $zname eq "장안" || $zname eq "양양" || $zname eq "낙양" || $zname eq "업" || $zname eq "허창" || $zname eq "건업" || $zname eq "한" || $zname eq "무도" || $zname eq "건녕" || $zname eq "안정" || $zname eq "한중" || $zname eq "검각" || $zname eq "자동" || $zname eq "강주" || $zname eq "영안" || $zname eq "홍농" || $zname eq "완" || $zname eq "강릉" || $zname eq "무릉" || $zname eq "영릉" || $zname eq "신야" || $zname eq "강하" || $zname eq "장사" || $zname eq "계양" || $zname eq "남해" || $zname eq "진유" || $zname eq "여남" || $zname eq "시상" || $zname eq "평원" || $zname eq "복양" || $zname eq "초" || $zname eq "수춘" || $zname eq "단양" || $zname eq "여강" || $zname eq "계" || $zname eq "남피" || $zname eq "소패" || $zname eq "북평" || $zname eq "북해" || $zname eq "하비" || $zname eq "광릉" || $zname eq "오" || $zname eq "운남" || $zname eq "양평" || $zname eq "국내" || $zname eq "사비" || $zname eq "매소" || $zname eq "서라벌" || $zname eq "천수" || $zname eq "졸본")){
							&K_LOG("$mmonth월 : [군사] : 해당 지역에서는 산월병을 뽑을 수가 없습니다..");
						}elsif("16" eq $csub && $zsub1 < 499){
							&K_LOG("$mmonth월 : [군사] : 농민병을 생산하기에는 기술력이 부족합니다.");
						}elsif("18" eq $csub && $zsub1 < 999){
							&K_LOG("$mmonth월 : [군사] : 극병을 생산하기에는 기술력이 부족합니다.");
						}elsif("19" eq $csub && $zsub1 < 749){
							&K_LOG("$mmonth월 : [군사] : 수병을 생산하기에는 기술력이 부족합니다.");
						}elsif("20" eq $csub && $zsub1 < 1099){
							&K_LOG("$mmonth월 : [군사] : 공병을 생산하기에는 기술력이 부족합니다.");
						}else{


						if($ggyo < 10){$ggyo=int(($cnum * 10)/30);}
							if($ksub1_ex == $csub){
								if($ksol + $cnum > ($kleat)*30){
									$cnum = int(($kleat)*30) - $ksol;
								}
								$ksol += $cnum;
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
							}else{
								if($cnum > ($kleat)*30){
									$cnum = $kleat*30;
								}
								$ksol = $cnum;
							}


							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /징병/){
										if($qup =~ /징병/){
										$kqpoint += $cnum;
										}else{
										$kqpoint += $qup;
										}
										&K_LOG("$mmonth월 : $qtalkd");
									}	
								}
							}


							$kgat -= int($cnum/30);
							if($kgat < 0 ){
								$kgat = 0;
							}
							$ksub1_ex = $csub;

							if($kcodea =~ /B6/ && $ksub1_ex == 6){
								$kqpoint += $cnum;
							}


							$kcex += 10;
							$kexp += 10;
							$kpoint += 4;

						if($kskill =~ /Bc/ && $csub == 7){
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/60);
						}elsif($kskill =~ /Bc/ && $kskill =~ /Fc/ && $csub == 7){
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/30);
						}elsif($kskill =~ /Fc/){
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/15);
						}else{
						$ggyo = int($cnum * ($SOL_PRICE[$csub] - $ga)/30);
						}


							$kgold -= $ggyo;




							if($kskill =~ /Db/ && $zpri >= 75){
							}else{
							$znum -= $cnum;
							}

							$zpri -= int($cnum / 300);
							if("$zname" ne ""){
								splice(@TOWN_DATA,$kpos,1,"$zname<>$zcon<>$znum<>$znou<>$zsyo<>$zshiro<>$znou_max<>$zsyo_max<>$zshiro_max<>$zpri<>$zx<>$zy<>$zsouba<>$zdef_att<>$zsub1<>$zsub2<>$z[0]<>$z[1]<>$z[2]<>$z[3]<>$z[4]<>$z[5]<>$z[6]<>$z[7]<>$zname1<>$zname2<>$zbong1<>$zbong2<>$zbong3<>\n");
							}

							&K_LOG("$mmonth월 : $SOL_TYPE[$ksub1_ex]를 <font color=red>+$cnum</font> 징병했습니다. [징병금액 : $ggyo]");
							if($cnum > 14){
							$kstr_ex++;
							$go_ex += int($kbank/5);
							}
							$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
						}
}
1;

