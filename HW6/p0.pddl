;; There is only one block, A, which is on the table.  A sprayer with
;; red paint is on the table.  Our goal is to have A be red and the
;; arm empty.

(define (problem 0)
	(:domain hw6)
	(:objects 
		block_a - Block
		red_spraycan - Spraycan
	)
	(:init 
		(arm-empty)
		
		;... there is a block A on the table with nothing on it...
		(on-table block_a)
		(clear block_a)
		
        ;... there is a red sprayer on the table with nothing on it...
		(on-table red_spraycan)
		(clear red_spraycan)
		(is-color red_spraycan RED)
	)
	
	(:goal 
		(and 
			(arm-empty)
            
			; ...A is red...
			(looks block_a RED)

						
        )
	)
)



