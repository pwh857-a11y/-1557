
sub JANGBI{
						$ksub2=0;						open(IN,"$ARM_LIST");
						@ARM_DATA = <IN>;
						close(IN);
						($armname,$armval,$armdmg,$armwei,$armele,$armsta,$armclass,$armtownid) = split(/<>/,$ARM_DATA[$cnum]);						($armname2,$armval2) = split(/<>/,$ARM_DATA[$karm]);
						$armval2 = int($armval2 * 0.6);
						if($armval > $kgold + $armval2){
							&K_LOG("$mmonth월 : $armname을 사기에는 소지금이 충분하지 않습니다.(금 : $armval)");
						}else{
							if($kcodea =~ /B8/){
							$kqpoint = 1;
							}
							$kgold += $armval2;
							$kgold -= $armval;
							$karm = $cnum;
							&K_LOG("$mmonth월 : 장비 : $armname2를 금 <font color=red>$armval2</font>로 팔아 $armname를 구입했습니다.");
							&MAP_LOG("<img src=$IMG/j22.gif> $kname님은 $armname을 구입했습니다.");
							&HISTORY_LOG($kid,"$armname을 구입했습니다.");
						}
}
1;

