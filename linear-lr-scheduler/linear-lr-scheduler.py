def linear_lr(step, total_steps, initial_lr, final_lr=0.0, warmup_steps=0) -> float:
    """
    Linear warmup (0→initial_lr) then linear decay (initial_lr→final_lr).
    Steps are 0-based; clamp at final_lr after total_steps.
    """
    # Write code here
    if step == 0 and total_steps!=0:
        lr_step = 0
    elif step==0 and total_steps ==0:
        lr_step = final_lr
    elif step<warmup_steps:
        lr_step = (step*initial_lr)/warmup_steps
    elif warmup_steps<=step<=total_steps:
        lr_step = final_lr + (initial_lr - final_lr)* ((total_steps-step)/(total_steps-warmup_steps))
    else:
        lr_step = final_lr

    return lr_step


        
    