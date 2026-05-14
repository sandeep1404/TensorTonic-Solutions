import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    # Write code here
    out = {}
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    fp = 0 
    fn = 0 
    tp =0 
    tn = 0 

    precision=[]
    recall=[]
    f1score =[]
    weights=[]
    
    tp_total = np.count_nonzero(np.equal(y_true,y_pred))
    
    acc = tp_total/len(y_true)
    out['accuracy'] = acc
    len_labels = len(np.unique(y_true))


    if average =='binary':
        indices = (np.where(y_true==pos_label)[0]) ## get the indexs of element for y_true 
        indice_ele = np.array(y_pred)[indices] ## get the elemts of those indexes in y_pred 

        tp = np.count_nonzero(np.where(indice_ele==pos_label,True, False))
        tn = tp_total - tp 
        

        indices_fp = (np.where(y_pred==pos_label)[0])
        fp_values = y_true[indices_fp]

        fp = np.count_nonzero(np.where(fp_values!=pos_label,True, False))
        fn = np.count_nonzero(np.where(indice_ele!=pos_label,True, False))


    for ele in np.unique(y_true):
        ## prediceted 0 consider 0 as positive but ideally its not correct so its false positive 0-->0 tp, 2(any number)-->0 fp 0-->1 fn considering 0 as positve and rest classes negative
    
        indices = (np.where(y_true==ele)[0]) ## get the indexs of element for y_true 
        indice_ele = y_pred[indices] ## get the elemts of those indexes in y_pred 
        
        indices_fp = (np.where(y_pred==ele)[0])
        fp_values = y_true[indices_fp]

        
        if average =='micro':
            tp += np.count_nonzero(np.where(indice_ele==ele,True, False)) ## 0-->0 tp, 1-->1 tn rest all classes even if same its tn 
            tn += tp_total - tp 
        
            ## fp and fn 
        
            fp += np.count_nonzero(np.where(fp_values!=ele,True, False))
        
            fn += np.count_nonzero(np.where(indice_ele!=ele,True, False))
        
        if average =='macro':
            tp = np.count_nonzero(np.where(indice_ele==ele,True, False)) ## 0-->0 tp, 1-->1 tn rest all classes even if same its tn 
            tn = tp_total - tp 
            
            ## fp and fn 
            
            fp = np.count_nonzero(np.where(fp_values!=ele,True, False))
            
            fn = np.count_nonzero(np.where(indice_ele!=ele,True, False))

            precision.append((tp)/(tp+fp))
            recall.append((tp)/(tp+fn))
            f1score.append((2*(tp))/ (2*tp+fp+fn))
        
        if average =='weighted':
            weights.append(len(np.where(y_true==ele)[0])/len(y_true))

            tp = np.count_nonzero(np.where(indice_ele==ele,True, False)) ## 0-->0 tp, 1-->1 tn rest all classes even if same its tn 
            tn = tp_total - tp 
            
            ## fp and fn 
            
            fp = np.count_nonzero(np.where(fp_values!=ele,True, False))
            
            fn = np.count_nonzero(np.where(indice_ele!=ele,True, False))

            precision.append((tp)/(tp+fp))
            recall.append((tp)/(tp+fn))
            f1score.append((2*(tp))/ (2*tp+fp+fn))

    



                    
   
    if average == 'macro':
        print(precision)
        precision = sum(precision)/len_labels
        recall = sum(recall)/len_labels
        f1score = sum(f1score)/len_labels
    
    elif average == 'weighted':
        weights = np.array(weights)
        print(weights)
        precision = np.array(precision)
        print(precision)
        recall = np.array(recall)
        f1score = np.array(f1score)
        
        precision = weights*precision
        print(precision)
        recall = weights*recall
        f1score = weights*f1score

        precision = sum(precision)
        print(precision)
        recall = sum(recall)
        f1score = sum(f1score)



    else:
        precision = (tp)/(tp+fp)
        recall = (tp)/(tp+fn)
        f1score =  2*(precision*recall)/ (precision+recall)

    out['precision'] = precision
    out['recall']= recall
    out['f1']= f1score

    return out    