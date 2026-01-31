
sub DOKRIP{
				$ksub2=0;
				if($zcon == 0 || $klevel < 10 || $zcon != $kcon){
					&K_LOG("이 도시에서는 독립할 수 없습니다.");
				}elsif($csub != $kpos){
					&K_LOG("현재지가 다릅니다.");
				}else{
				open(IN,"$COUNTRY_NO_LIST") or &ERR2('파일을 열지 않았습니다. err no :country');
				@COU_NO_DATA = <IN>;
				close(IN);
					$d_hit=0;
					foreach(@DEF_DATA){
						($mdid,$mdname,$mdtown_id,$mdtown_flg,$mdcon,$mdchara,$mdsol,$mdsub1_ex) = split(/<>/);
						if($cnum eq $mdtown_id){
							$d_hit++;
						}
					}
					if( $kclass >= 5000 && 100-$zpri-$d_hit*10 > int(rand(100))){
						foreach(@COU_DATA){
							($xcid,$xname,$xele,$xmark,$xking,$xmes,$xsub,$xpri)=split(/<>/);
							$ele{$xele} = 1;
						}
						while(){
							$rnd_max = @ELE_C-1;
							$r = int(rand($rnd_max))+1;
							if( $ele{$r} != 1 ){
								$cend = $r;
								last;
							}
						}
						$COU_NO_DATA = @COU_NO_DATA + 1;
						$kcon = $COU_NO_DATA;

						&TOWN_DATA_OPEN("$kpos");
						$zcon = $COU_NO_DATA;
						&TOWN_DATA_INPUT;

						$zcon = $COU_NO_DATA;
						push(@COU_DATA,"$COU_NO_DATA<>$cnum<>$cno<>55<>$kid<><><>1<>\n");
						open(OUT,">$COUNTRY_LIST") or &E_ERR('COUNTRY 데이터를 기입할 수 없습니다.');
						print OUT @COU_DATA;
						close(OUT);

						push(@COU_NO_DATA,"$COU_NO_DATA<>$cnum<>$cno<>55<>$kid<><><>1<>\n");
						open(OUT,">$COUNTRY_NO_LIST") or &E_ERR('COUNTRY 데이터를 기입할 수 없습니다.');
						print OUT @COU_NO_DATA;
						close(OUT);

						&K_LOG("$cnum국을 건국했습니다.");
						&MAP_LOG2("<font color=000088><B>[독립]</B></font> $kname님은 반란에 성공해 $zname을 도읍으로 한 $cnum국을 건국하였습니다.");
						&MAP_LOG("<font color=000088><B>[독립]</B></font> $kname님은 반란에 성공해 $zname을 도읍으로 한 $cnum국을 건국하였습니다.");
						&HISTORY_LOG($kid,"반란이 성공하여 $cnum국을 건국하였습니다.");
						&TOWN_CHANGE($kpos);

					}else{
						&TOWN_CHANGE($kpos);
						&BONG_DEL;
						&DELETE;
						&MAP_LOG("<font color=000088><B>[실패]</B></font>$zname성에서 반란이 실패하여 $kname님은 역모죄로 처형되었습니다.");
						$zpri -= (int(rand($zpri/20))+int(rand($zpri/20))+1);
					}
				}	
}
1;

