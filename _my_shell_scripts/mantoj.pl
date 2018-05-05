#!/usr/bin/perl

$file = $ARGV[0];
$lang = $ARGV[1];
#print("#$file#$lang#\n");

my $var;
my $var_new;


  my $fhr;
  my $fhw;
  local $/;

  my $add_txt = '';

  if ("$lang" eq "DE") {
    $add_txt = '<p><strong>Quelle:<br /></strong>Spirit Voyage ' . 
    '(<a href="https://www.spiritvoyage.com/mantra/">https://www.spiritvoyage.com/mantra/</a>), ' .
    '&Uuml;bersetzung von Prabhudhan Singh</p>';  
  } else {
    $add_txt = '<p><strong>Source:<br /></strong>Spirit Voyage ' . 
    '(<a href="https://www.spiritvoyage.com/mantra/">https://www.spiritvoyage.com/mantra/</a>)</p>';  
  }
  open($fhr, '<', $file) || die "R: can't open $file: $!";
  $var_tmp = <$fhr>;
  close($fhr);

  $var_tmp =~ s/:<\/b><\/p>\n<p>/:<\/b><br>\n/g;
  $var = $var_tmp . $add_txt;

  open($fhw, '>', $file) || die "W: can't open $file: $!";
  print $fhw $var;
  close($fhw);
