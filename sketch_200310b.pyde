def setup():
    size(400, 400)
    x_size=400
    y_size=400
    background(255,255,255)     
    
    x_middle_point = x_size/2
    y_adjust_point = 50    
    strokeWeight(4) 
    stroke(0,0,0)    
    strokeJoin(MITER)
     
#    line(x_middle_point,-40 + y_adjust_point ,x_middle_point-10, -40+y_adjust_point)
    
    #line(x_middle_point,-20 + y_adjust_point ,x_middle_point-10, 30+y_adjust_point)
    #line(x_middle_point,-20 + y_adjust_point ,x_middle_point+10, 30+y_adjust_point)
    #beginShape();
    #fill(0,128,255) #blue
    #vertex(x_middle_point,-20 + y_adjust_point); 
    #vertex(x_middle_point-10, 30+y_adjust_point); 
    #vertex(x_middle_point+10, 30+y_adjust_point);
    #vertex(x_middle_point,-20 + y_adjust_point); 
    #endShape();
   

    #head
    fill(0,128,255) #blue
    arc(x_middle_point,130 + y_adjust_point ,200,200,radians(135),radians(405))
   
    #face white
    fill(255,255,255)
    arc(x_middle_point,150 + y_adjust_point ,185,170,radians(120),radians(300))
    arc(x_middle_point,150 + y_adjust_point ,190,170,radians(280),radians(410))
    
    #left eye
    fill(255,255,255) #white
    ellipse(x_middle_point-20, 70 + y_adjust_point , 40, 50)
    
    #left eye black
    fill(0,0,0)
    ellipse(x_middle_point-10, 72 + y_adjust_point , 9, 12) 
    
    #right eye
    fill(255,255,255)
    ellipse(x_middle_point+20, 70 + y_adjust_point , 40, 50) 
    
    #right eye black
    fill(0,0,0)
    ellipse(x_middle_point+10, 72 + y_adjust_point , 9, 12) 
    
    #nose
    fill(255,0,0) 
    ellipse(x_middle_point, 100 + y_adjust_point , 25, 25)
    
    #nose line
    line(x_middle_point,112 + y_adjust_point ,x_middle_point,175+ y_adjust_point)
    
    #mouse line
    noFill()
    arc(x_middle_point, 138 + y_adjust_point , 120, 80,  radians( -10 ), radians( 190 ) , OPEN)
    
    #cat beard
    #right
    line(x_middle_point+45,110 + y_adjust_point ,x_middle_point+70,106 + y_adjust_point )
    line(x_middle_point+47,122 + y_adjust_point ,x_middle_point+70,122 + y_adjust_point )
    line(x_middle_point+45,135 + y_adjust_point ,x_middle_point+70,138 + y_adjust_point )
    #left
    line(x_middle_point-45,110 + y_adjust_point ,x_middle_point-70,106 + y_adjust_point )
    line(x_middle_point-47,122 + y_adjust_point ,x_middle_point-70,122 + y_adjust_point )
    line(x_middle_point-45,135 + y_adjust_point ,x_middle_point-70,138 + y_adjust_point )
   
    #body
    fill(0,128,255) #blue
    quad(x_middle_point-78,200 + y_adjust_point ,
         x_middle_point+78,200 + y_adjust_point , 
         x_middle_point+88,300 + y_adjust_point , 
         x_middle_point-88,300 + y_adjust_point );
   
    #bell 
    fill(255,204,51) 
    ellipse(x_middle_point, 220 + y_adjust_point , 28, 28)
    rect(x_middle_point-12, 217 + y_adjust_point , 24, 4, 7)
    fill(0,0,0) 
    ellipse(x_middle_point, 227 + y_adjust_point , 5, 5)
   
    #neck
    fill(255,0,0) 
    rect(x_middle_point-78,200 + y_adjust_point , 158, 8, 3)
   
    #pocket
    fill(255,255,255) 
    arc(x_middle_point,240 + y_adjust_point ,100,100 ,0 , PI , CHORD)
    
    #hands
    ellipse(x_middle_point-80,250  + y_adjust_point , 40, 40)
    ellipse(x_middle_point+80,250  + y_adjust_point , 40, 40)
    
    save("drawing.png");
