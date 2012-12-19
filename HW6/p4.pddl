;; Block A is on the table, B is on A and C on B.  On the table are a
;; watr bucket, a red sprayer, cans of blue and green paint and a
;; clean brush.  The goal is to make A red, B green and C blue and to
;; have A on B, B on C and C on the table and the brush clean and arm
;; empty.

(define (problem 4)
	(:domain hw6)
	
	(:objects 
		;3 blocks
		block_a - Block
		block_b - Block
		block_c - Block
		
		;1 red sprayers 
		red_sprayer - Spraycan
		
		;2 paint cans...blue and green
		blue_paint_can - PaintCan
		green_paint_can - PaintCan
		
		;1 paint brush
		paint_brush - PaintBrush
		
		;1 water bucket
		water_bucket - WaterBucket
	)
  
	(:init 		
		(arm-empty)
        
		;Block A is on the table, B is on A and C on B
		(on-table block-a)
		(on block-b block_a)
		(on block-c block_b)
		(clear block_c)
		
		
		;rest of the objects are all on the table
		(on-table red_sprayer)
		(on-table green_paint_can)
		(on-table blue_paint_can)
		(on-table paint_brush)
		(on-table water_bucket)
		
		(clear red_sprayer)
		(clear green_paint_can)
		(clear blue_paint_can)
		(clear paint_brush)
		(clear water_bucket)
		
		;defining colors for the spraycans and paint cans
		(is-color red_sprayer RED)
		
		(is-color green_paint_can GREEN)
		(is-color blue_paint_can BLUE)		
		
		
		;brush is initially clean
		(clean paint_brush)
		(is-color paint_brush NONE)
	)
  
	(:goal 
		(and 
			(arm-empty) 
			
			;A red, B green and C blue
			; have A on B, B on C and C on the table			
					
			(looks block_c BLUE)
			(on-table block_c)
			
			(looks block_a RED)
			(on block_a block_b)
			(clear block_a)
			
			(looks block_b GREEN)
			(on block_b block_c)			
			
						
			
			
			;the brush clean 
			(clean paint_brush)
			(is-color paint_brush NONE)
		)
	)
)


