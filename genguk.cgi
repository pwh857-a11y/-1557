
sub GENGUK{
				$ksub2=0;
				if($zcon != 0){
					&K_LOG("이 도시에서는 기양할 수 없습니다.");
				}elsif($csub != $kpos){
					&K_LOG("현재지가 다릅니다.");
				}else{
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
					$COU_NO_DATA++;
					$kcon = $COU_NO_DATA;
					$zcon = $COU_NO_DATA;
					push(@COU_DATA,"$new_cou_no<>$in{'cou_name'}<>$in{'ele'}<>1<>$in{'id'}<><>$in{'chara_name'}<>1<>\n");

					&K_LOG("$mmonth월 : $cnum국을 건국했습니다.");
					&MAP_LOG2("<font color=000088><B>[건국]</B></font> $kname님은 $cnum국을 건국하였습니다.");
					&MAP_LOG("<font color=000088><B>[건국]</B></font> $kname님은 $zname성을 도읍으로 한 $cnum국을 건국하였습니다.");
					&HISTORY_LOG($kid,"$cnum국을 건국하였습니다.");
					&TOWN_CHANGE($kpos);
				}	
}
1;

