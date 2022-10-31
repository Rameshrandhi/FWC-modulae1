module flash(
  input A,
  input B,
  output wire r,
  output wire g,

);
reg r.g;
always@(A,B)
begin
  r=(!A&&B) || (!B&&A);
  g= (A&&B);
  
end
endmodule
