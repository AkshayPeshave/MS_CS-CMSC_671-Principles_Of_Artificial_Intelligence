;; Block A is on the table, block B on A and there is nothing on B.  A
;; water bucket, a brush, a A blue sprayer and a red paint can are on
;; the table and clear.  The goal is to for A to be colored ref and B
;; blue and the brush be clean. 

(define (problem 2)
	(:domain hw6)
	(:objects
		block_a - Block
		block_b - Block
		blue_sprayer - Spraycan
		red_paint_can - PaintCan
		paint_brush - PaintBrush
		water_bucket - WaterBucket
	)
  
	(:init (arm-empty)
        ;... block A is on the table ...
		(on-table block_a)
		
		;... block B is on block A and there's nothing on B ...
		(on block_b block_a)
		(clear block_b)
		
        ;... there is a blue sprayer on the table and nothing is on it ...
		(on-table blue_sprayer)
		(clear blue_sprayer)
		(is-color blue_sprayer BLUE)
		
		;... there is a red paint can on the table and noting is on it ...
		(on-table red_paint_can)
		(clear red_paint_can)
		(is-color red_paint_can RED)
		
		;... there is a clean brush on the table and nothing is on it  ...
		(on-table paint_brush)
		(clear paint_brush)
		(clean paint_brush)
		(is-color paint_brush NONE)
		
		;... there is a water bucket on the table and nothing is on it ...
		(on-table water_bucket)
		(clear water_bucket)
		
      )
	(:goal 
		(and 			
            ;... A is red ...
			(looks block_a RED)
			
            ;... B is blue ...
			(looks block_b BLUE)
			
            ;... the brush is clean ...
			
			(clean paint_brush)
			(is-color paint_brush NONE)
        )
	)
)





