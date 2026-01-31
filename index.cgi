#!C:\xampp\perl\bin\perl.exe

use lib 'C:/xampp/htdocs';

# --- Modern HTML shell (added) ---------------------------------------------
if(($ENV{'QUERY_STRING'} || '') !~ /(?:^|&)legacy=1(?:&|$)/){
    # (legacy/broken lines kept for history)
    # print "Content-type: text/html
    #     # ";
    print "Content-type: text/html\n\n";
    print <<"HTMLTAG";
<!doctype html>
<html lang="ko">
<head>
<meta charset="euc-kr">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="./static/modern.css">
<title>Samgugji NET</title>
</head>
<body>
<div style="max-width:900px;margin:10vh auto;padding:24px;border:1px solid rgba(255,255,255,.14);border-radius:14px;background:rgba(255,255,255,.04)">
<h2 style="margin:0 0 8px">Samgugji NET</h2>
<p style="margin:0 0 16px;color:rgba(255,255,255,.75)">Loading...</p>
<a href="dkajlfjeioaefhoiwqhfeouihwefwefksdjklfjwe.cgi" style="display:inline-block;padding:10px 14px;border:1px solid rgba(255,255,255,.18);border-radius:12px">Enter</a>
</div>
<script>location.replace('dkajlfjeioaefhoiwqhfeouihwefwefksdjklfjwe.cgi');</script>
<noscript><div style="text-align:center;">JavaScript is disabled. Please click Enter.</div></noscript>
</body>
</html>
HTMLTAG
    exit;
}
# --- Legacy frameset below --------------------------------------------------

print "Content-type: text/html\n\n";
print<<"HTMLTAG";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Frameset//EN">
<html>
<head>
    <link rel="shortcut icon" href="samgug.ico">
    <title>ﱹ  NET - ĥ</title>
</head>
<frameset rows="99%,1" frameborder=0 border=0 framespacing=0>
    <frame src="dkajlfjeioaefhoiwqhfeouihwefwefksdjklfjwe.cgi" name="Main">
</frameset>
</html>
HTMLTAG
exit;