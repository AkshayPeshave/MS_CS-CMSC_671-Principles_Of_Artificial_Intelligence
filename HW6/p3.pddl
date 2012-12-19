;; three blocks (A B and C) are on the table along with three sprayers
;; (red, green, blue), three paint cans (red, green, blue), a water
;; bucket and a clean brush.  Paint A, B and C red, blue and green,
;; respectively. End with the arm empty and the brush clean.

(define (problem 3)
	(:domain hw6)
	
	(:objects 
		;3 blocks
		block_a - Block
		block_b - Block
		block_c - Block
		
		;3 sprayers RGB
		red_sprayer - Spraycan
		blue_sprayer - Spraycan
		green_sprayer - Spraycan
		
		;3 paint cans RGB
		red_paint_can - PaintCan
		blue_paint_can - PaintCan
		green_paint_can - PaintCan
		
		;1 paint brush
		paint_brush - PaintBrush
		
		;1 water bucket
		water_bucket - WaterBucket
	)
	(:init 
		(arm-empty)
        
		;all objects on the table and clear
		(on-table block-a)
		(on-table block-b)
		(on-table block-c)
		(on-table red_sprayer)
		(on-table green_sprayer)
		(on-table blue_sprayer)
		(on-table red_paint_can)
		(on-table green_paint_can)
		(on-table blue_paint_can)
		(on-table paint_brush)
		(on-table water_bucket)
		
		(clear block-a)
		(clear block-b)
		(clear block-c)
		(clear red_sprayer)
		(clear green_sprayer)
		(clear blue_sprayer)
		(clear red_paint_can)
		(clear green_paint_can)
		(clear blue_paint_can)
		(clear paint_brush)
		(clear water_bucket)
		
		;defining colors for the spraycans and paint cans
		(is-color red_sprayer RED)
		(is-color green_sprayer GREEN)
		(is-color blue_sprayer BLUE)
		
		(is-color red_paint_can RED)
		(is-color green_paint_can GREEN)
		(is-color blue_paint_can BLUE)		
		
		;brush is initially clean
		(clean paint_brush)
		(is-color paint_brush NONE)
	)
  
	(:goal 
		(and 
			(arm-empty)
			
			;... a is red
			(looks block_a RED)
			
			;b is blue
			(looks block_b BLUE)
			
			;C is green
			(looks block_c GREEN)
			
			;the brush is clean...
			(clean paint_brush)
			(is-color paint_brush NONE)
		)
	)
)
    




