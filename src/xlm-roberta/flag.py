import argparse

def get_parser():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-n", "--epochs", default=1, type=int, metavar='N', help='Number of total epochs to run')
    parser.add_argument("-train_batch", "--train_batch_size", default=16, type=int, metavar='N', help='Train-mini-batch size')
    parser.add_argument("-valid_batch", "--valid_batch_size", default=32, type=int, metavar='N', help='Valid-mini-batch size')
    parser.add_argument("-ml", "--max_len", default=128, type=int, metavar='N', help='Max number of words in a question to use')
    
    parser.add_argument("-lr", "--learning_rate", default=3e-5, type=float, metavar='LR', help='Initial learning rate')
    parser.add_argument("-wd","--weight_decay", default=1e-4, type=float, metavar='W', help='Weight Decay')
    
    parser.add_argument("-hs", "--hidden_size", default=64, type=int, metavar='N', help='Rnn hidden size')
    parser.add_argument("-rs", "--reduction_size", default=16, type=int, metavar='N', help='Rnn reduction size')
    parser.add_argument("-nl", "--num_layers", default=1, type=int, metavar='N', help='Number of rnn layers')
    parser.add_argument("--classes", default=1, type=int, metavar='N', help='Number of output classes')
    parser.add_argument("--training_file", default='/content/drive/MyDrive/Multimodal-Hate-Speech-Bengali/data/train_text.csv',type=str, help='Path to train file')
    parser.add_argument("--testing_file", default='/content/drive/MyDrive/Multimodal-Hate-Speech-Bengali/data/test_text.csv',type=str, help='Path to test file')
    parser.add_argument("--validation_file", default='/content/drive/MyDrive/Multimodal-Hate-Speech-Bengali/data/validate_text.csv',type=str, help='Path to validation file')
    parser.add_argument("-do", "--dropout", type=float, default=0.1,help="dropout")
    parser.add_argument("-m_path", "--model_path", type=str, default='/content/drive/MyDrive/Multimodal-Hate-Speech-Bengali/src/xlm-roberta/store_model/',help="Save best model")
    parser.add_argument("--seed", type=int, default=42,help="seed for reproducibility")
    parser.add_argument("--clip", type=float, default=0.25, help='Gradient clipping')
    
    parser.add_argument("--output", default='pred.csv',type=str, help='Path to output file')
    
    parser.add_argument("--model_specification", default="xlm-roberta-large", required=False, help="model name")
    parser.add_argument("--model_layer", default='last_two',type=str, help='Model layer')
    parser.add_argument("--pretrained_model_name", default="xlm-roberta-large", required=False, help="Pretrained model name")
    parser.add_argument("--roberta_hidden", default=1024, type=int, metavar='N', help='Number of layer for bert')
    parser.add_argument("--adam_epsilon", default=1e-8, type=float, help="Epsilon for Adam optimizer.")
    parser.add_argument("--warmup_steps", default=0, type=int, help="Linear warmup over warmup_steps.")
    #args = parser.parse_args()
    return parser

