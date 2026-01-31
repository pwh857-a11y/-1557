#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';
require 'jcode.pl';
require './ini_file/index.ini';
require 'suport.cgi';

if($MENTE) { &ERR2("\xb7Œµ\xf9\xc1\xdf\xc0\xd4\xb4\xcf\xb4\xd9. \xc0\xe1\xbd√∏\xb8 \xb1\xe2\xb4\xd9\xb7\xc1 \xc1\xd6\xbc\xbc\xbf\xe4."); }
&DECODE;
&SERVER_STOP;
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("\xc1\xd6\xbc\xd2\xc3\xa2\xbf\xa1 \xb0\xaa\xc0\xbb \xc0\xd4\xb7\xc2\xc7\xcf\xc1\xf6 \xb8\xbb\xbe\xc6\xc1\xd6\xbc\xbc\xbf\xe4."); }

if($mode eq '' || $mode eq 'PLAN') { &PLAN; }
elsif($mode eq 'PLAN_SAVE') { &PLAN_SAVE; }
else { &ERR("\xbf\xf9\xb8\xae\xc1\xf6 \xbe\xca\xc0\xba \xbe\xd7\xbc\xbc\xbd\xba\xc0\xd4\xb4\xcf\xb4\xd9."); }

sub PLAN {
  &CHARA_MAIN_OPEN;
  &TIME_DATA;
  my $cmd_path = "./charalog/command/$kid\.cgi";
  my @CUR = ();
  if (open(my $IN, $cmd_path)) { @CUR = <$IN>; close($IN); }

  # Normalize to 30 lines
  for(my $i=0; $i<30; $i++) { $CUR[$i] = '' if (!defined $CUR[$i]); }

  my %OPT = (
    26 => 'ú¥ãù',
    1  => 'ÜçóÖ',
    2  => 'ÉÅóÖ',
    29 => 'Í∏∞Ïà†',
    8  => 'Í∏',
    30 => 'àòÎπÑÎ',
    12 => 'Î∞©Ïñ¥ãúÑ§',
    3  => 'Ñ±Î≤ΩÍ∞ïôî',
    17 => \'¿Ãµø\',
    18 => \'√‚∫¥\',
  );

  &HEADER;
  print "<title>30Ñ¥ òàïΩ Ïª§Îß®ìú</title>\n";
  print "</head><body>\n";
  print "<div class=\"card\" style=\"max-width:980px;margin:16px auto\">";
  print "<h2 style=\"margin:0 0 8px 0\">30Ñ¥ òàïΩ Ïª§Îß®ìú</h2>";
  print "<div style=\"opacity:.85;margin-bottom:10px\">òÑû¨ Î°úÍ∑∏ù∏: <b>$kname</b> ($kid) / ù¥ òàïΩ <b>Ç¥ Ïª§Îß®ìú ååùº(30Ï§)</b>ùÑ çÆñ¥îÅãàã§.</div>";
  print "<form method=post action=./plan.cgi>\n";
  print "<input type=hidden name=mode value=PLAN_SAVE>\n";
  print "<input type=hidden name=id value=\"$kid\">\n";
  print "<input type=hidden name=pass value=\"$kpass\">\n";

  print "<div style=\"display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:10px 0\">";
  print "<label>Îπ†Î•∏ †Åö©:</label>";
  print "<select id=quickSel>";
  foreach my $mid (sort {$a<=>$b} keys %OPT) {
    print "<option value=\"$mid\">$OPT{$mid}</option>";
  }
  print "</select>";
  print "<button type=button class=\"btn\" onclick=\"applyAll()\">30Ïπ∏Ïóê èôùº †Åö©</button>";
  print "<button type=submit class=\"btn\">û•</button>";
  print "<a class=\"btn\" href=\"./status.cgi?id=$kid&pass=$kpass&mode=STATUS\">èåïÑÍ∞Í∏</a>";
  print "</div>";

  print "<table class=\"table\" style=\"width:100%\">";
  print "<thead><tr><th style=\"width:70px\">ä¨Î°</th><th>Î™ÖÎ†π</th><th>¥ÎªÛµµΩ√</th></tr></thead><tbody>";
  for(my $i=0; $i<30; $i++) {
    my $line = $CUR[$i];
    my $cur_mid = 26;
    if ($line ne '') {
      my @p = split(/<>/, $line);
      $cur_mid = int($p[0]||26);
    }
    print "<tr><td>".($i+1)."Ñ¥</td><td>";
    print "<select name=\"cmd".($i+1)."\" class=\"input\">";
    foreach my $mid (sort {$a<=>$b} keys %OPT) {
      my $sel = ($mid == $cur_mid) ? ' selected' : '';
      print "<option value=\"$mid\"$sel>$OPT{$mid}</option>";
    }
        print "</select>";
    my $cur_targ = 0;
    if ($line ne '') {
      my @pp = split(/<>/, $line);
      $cur_targ = int($pp[4]||0);
    }
    print " <select name=\"targ".($i+1)."\" class=\"input\">";
    print "<option value=\"\">-</option>";
    my $tn = scalar(@town_name);
    for(my $t=0; $t<$tn; $t++){
      my $sel2 = ($t == $cur_targ) ? ' selected' : '';
      my $nm = $town_name[$t];
      $nm =~ s/\"/&quot;/g;
      print "<option value=\"$t\"$sel2>$t. $nm</option>";
    }
    print "</select>";
    print "</td></tr>";

  }
  print "</tbody></table>";
  print "</form>";
  print "</div>";
  print "<script>
function applyAll(){
  var v = document.getElementById('quickSel').value;
  for(var i=1;i<=30;i++){
    var el = document.querySelector('select[name="cmd'+i+'"]');
    if(el) el.value = v;
  }
}
</script>";
  print "</body></html>";
}

sub PLAN_SAVE {
  &CHARA_MAIN_OPEN;
  &TIME_DATA;
  my $cmd_path = "./charalog/command/$kid\.cgi";
  my $now = time;
  my $rest_sym = "\xBC\xF6\xBB\xF6"; # legacy-safe placeholder (same bytes used by bot init)

  my %TOK = (
    17 => '__MOVE__',
    18 => '__ATTACK__',
    1  => '__AGRI__',
    2  => '__COMM__',
    29 => '__TECH__',
    8  => '__RICE__',
    30 => '__GARRISON__',
    12 => '__DEF__',
    3  => '__CASTLE__',
    26 => $rest_sym,
  );

  # ensure dir
  unless(-d "./charalog/command") { mkdir("./charalog/command", 0777); }

  if (open(my $OUT, ">$cmd_path")) {
    eval { flock($OUT, 2); };
    for(my $i=1; $i<=30; $i++) {
      my $mid = int($in{"cmd$i"} || 26);
      if (!defined $TOK{$mid}) { $mid = 26; }
      my $sym = $TOK{$mid};
      print $OUT "$mid<><>$sym<>$now<><><><><>\n";
    }
    close($OUT);
    chmod(0666, $cmd_path);
  }

  &HEADER;
  print "<title>û• ôÑÎ£</title></head><body>";
  print "<div class=\"card\" style=\"max-width:680px;margin:16px auto\">";
  print "<h2 style=\"margin:0 0 8px 0\">30Ñ¥ òàïΩ û• ôÑÎ£</h2>";
  print "<div style=\"margin:10px 0\">ã§ùå Ñ¥Î∂Ñ∞ òàïΩêú Ïª§Îß®ìúÍ∞ àúÑúÎ° †Åö©ê©ãàã§.</div>";
  print "<a class=\"btn\" href=\"./plan.cgi?id=$kid&pass=$kpass&mode=PLAN\">ã§ãú é∏Ïß</a> ";
  print "<a class=\"btn\" href=\"./status.cgi?id=$kid&pass=$kpass&mode=STATUS\">ÉÅÉúÎ°</a>";
  print "</div></body></html>";
}
