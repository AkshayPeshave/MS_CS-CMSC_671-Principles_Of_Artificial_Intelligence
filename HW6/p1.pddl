;; There is only one block, A, which is on the table.  A can with
;; red paint is on the table.  There is a clean brush on the
;; table.  Our goal is to have A be red and the arm empty.

(define (problem 1)
	(:domain hw6)
	(:objects
		block_a - Block
		red_paint_can - PaintCan
		paint_brush - PaintBrush
	)
  
	(:init (arm-empty)
		;... block A on the table with nothing on it ...
		(on-table block_a)
		(clear block_a)
		;(Block block_a)
		
		;... a red paint can on the table with nothing on it ...
		(on-table red_paint_can)
		(clear red_paint_can)
		(is-color red_paint_can RED)
		
		;... a clean brush is on the table with nothing on it ...
		(on-table paint_brush)
		(clear paint_brush)
		(clean paint_brush)
		(is-color paint_brush NONE)
	)
	
	(:goal 
		(and 
			(arm-empty)
            
			;... A is red ...
			(looks block_a RED)
			
			
        )
	)
)



