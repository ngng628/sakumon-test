#!/usr/bin/env ruby

n = gets.to_i
a = [n, 9].min
b = n - 1 - a
puts "#{a} #{b}"
