
sub SUSAEK{


							open(IN,"$QUEST_DATA");
							@QUEST_DATA = <IN>;
							close(IN);

							foreach(@QUEST_DATA){
							($qnum,$qcode,$qface,$qname,$qlevel,$quest,$qlimit,$qtalka,$qtalkb,$qtalkc,$qgold,$qrice,$qstr,$qint,$qlea,$qcha,$qcex,$qexp,$qseal,$qflag,$qcategory,$qrate,$qtalkd,$qup) = split(/<>/);
								if($kcodea =~ /$qcode/ && $qrate > rand(99)){
									if($qcategory =~ /수색/){
										$kqpoint += $qup;
										if($qtalkd eq ""){
										}else{
										&K_LOG("$mmonth월 : $qtalkd");
										}
									}	
								}
							}

							if($kcodea =~ /A5/){
								$kqpoint += 1;
							}
				$rmax = int(320 - ($kchat*2));
				if($rmax < 220 ){
					$rmax = 220;
				}
				$r = int(rand($rmax));
				if($kcodea =~ /A7/ && $r < 30){
				$kqpoint += 1;
				&K_LOG("깊은 산 속에서 설비향의 비녀를 찾았습니다!");
				}elsif( $r < 40 ){				
					$getgold = int(rand(50+$kchat))+50;
					$kgold += $getgold;
					&K_LOG("수색중에 금 <font color=red>$getgold</font>돈을 찾아내었습니다.");
				}elsif( $r < 46 ){
					if( int(rand(100+$kstrt)) > 100 ){
						$kstr += 1;
						&K_LOG("수색중에 호랑이가 덮쳐왔습니다!\n그러나 $kname님은 호랑이를 베어 물리쳤습니다.\n무력이 <font color=red>+1</font> 상승하였습니다.");
					}else{
						&K_LOG("수색중에 호랑이가 덮쳐왔습니다!\n그러나 $kname님은 도망갔습니다..");
					}
				}elsif( $r < 54 ){
					if( int(rand(100+$kstr)) > 100 ){
						$getgold = int(rand(50+$kchat))*2+200;
						$kgold += $getgold;
						&K_LOG("탐색중에 산적이 덮쳐왔습니다!\n그러나 $kname는 산적을 토벌하는데 성공했습니다.\n마을주민들이 「$kname님, 우릴 못살게 굴던 산적을 퇴치해주셔서 감사합니다. 작지만 받아주십시오!」 금 <font color=red>$getgold</font>을 받았습니다!");
					}else{
						&K_LOG("탐색중에 산적이 덮쳐왔습니다! $kname님은 패배하고 도망갔습니다.");
					}
				}elsif( $r < 59 ){
					$getgold = int(rand(200-$kchat/2))+10;
					$kgold -= $getgold;
					if( $kgold < 0 ){
						$getgold = -$kgold;
						$kgold = 0;
					} 
					&K_LOG("수색중에 금 <font color=red>$getgold</font>를 흘려버리고 말았습니다!");
				}elsif( $r < 65 ){
					if( rand(25) < 1 ){
						$getpwr = +1;
						$kstr += $getpwr;
						$kint += $getpwr;
						$klea += $getpwr;
						$kcha += $getpwr;
						&K_LOG("탐색중에 한 노인이 다가왔습니다. 「이 늙은이의 이름은 우길이라고 합니다. 그대는 잠재능력을 가지고 있으니 저에게 맡겨줘보십시오.」 모든 능력치가 <font color=red>$getpwr</font> 상승하였습니다.");
					}
				}elsif( $r < 75 ){
					$rnd = int(rand($kchat+100));
					if( $rnd > 50 ){
						$kcha_ex += 5;
						&K_LOG("수색중에 울고 있는 남자애를 찾아내었습니다.\n아무래도 부모를 잃어버린 것 같습니다.\n$kname님은 1시간 부근을 수색한 결과, 그 아이의 부모를 찾아낼 수가 있었다.\n매력경험치가 <font color=red>+5</font> 상승하였습니다.");
					}else{
						&K_LOG("수색중에 울고 있는 남자애를 찾아내었습니다.\n아무래도 부모를 잃어버린 것 같습니다.\n$kname님은 1시간 부근을 수색했지만 유감스럽게도 그 아이의 부모는 찾아낼 수가 없었다.\n가까운 마을사람에게 그 아이를 맡기고는 $kname님은 떠났습니다.");
					}
				}elsif( $r < 85 ){
					$kcha_ex += 3;
					&K_LOG("수색중에 연회에 권유를 받았습니다.\n「$kname공, 지금 연회의 분위기가 무르있고 있는데 $kname공도 참가해주시오.」\n마을사람으로부터 술을 권유받고 즐거운 시간을 보냈습니다.\n매력경험치가 <font color=red>+3</font> 상승하였습니다.");
				}elsif( $r < 100 ){
					$kint_ex += 3;
					&K_LOG("수색중에 한 사람의 청이 있었습니다.\n「$kname님, 우리는 우매하여 글자를 읽을수가 없습니다. 지도를 부탁드립니다!」 \n$kname는 기분좋게 허락해 강의를 열었다.\n이에 민중들은 몹시 기뻐하였습니다.\n지력경험치가 <font color=red>+3</font> 상승하였습니다.");
				}elsif( $r < 120 ){
					&K_LOG("활짝 개인 푸른하늘 아래 $kname는 풍류를 즐기며 한가로이 시간을 보냈다. 모든 능력치의 경험치가 <font color=red>+1</font> 상승하였습니다.");
					$kstr_ex += 1;
					$kint_ex += 1;
					$klea_ex += 1;
					$kcha_ex += 1;
				}elsif( $r < 200 ){
					$kcha_ex += 1;

					@rmes = (
					"들은 이야기로는 훈련이 낮으면 군사도 꽤 약해진답니다.",
					"들은 이야기로는 정찰이 대성공을 하게 되면 누구의 계략인지 모르게 되는 것 같더군요.",
					"파괴는 성벽치가 높으면 성공하기 힘듭니다만 성공하게 되면 효과는 큰 것 같습니다.",
					"탐색중에 선인을 만나면 능력치를 올려주는 일도 있는 것 같습니다.",
					"적을 격파하면 상대의 소지품을 빼앗을 수도 있습니다.",
					"민심을 잘 잡아두면 병역 인구가 증가하기 쉽답니다.",
					"경지가 많으면 인구가 증가하기 쉽습니다.",
					"상업이 발전하고 있으면 사람이 모여듭니다.",
					"녹봉은 현재 주둔 중인 도시로부터 돈이 나타납니다.",
					"소지품은 2개밖에 가질 수 없기 때문에 조심하슈."
					);
					$r = int(rand(@rmes));
					&K_LOG("탐색중에 마을사람을 만났습니다.\n마을사람:「$rmes[$r]」");
				}else{
				&K_LOG("아무 것도 발견되지 않았습니다.");
				}
				$ksub1 = "$kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex,$bo_ex,$gi_ex,$ch_ex,$gu_ex,$go_ex,$jin_ex,";
					
}
1;

