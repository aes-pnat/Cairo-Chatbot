from torch.utils.data import Dataset
import json

class FinanceDataset(Dataset):
    def __init__(self, path:str, tokenizer):
        self.data = json.load(open(path, "r"))

        self.X = []
        for i in self.data["rows"]:
            self.X.append(i['row']['sentence'])

        for idx, i in enumerate(self.X):
            try:
                self.X[idx] = "<startofstring> "+i+" <bot>: "+self.X[idx+1]+" <endofstring>"
            except:
                break

        self.X = self.X[:5000]
        
        print(self.X[0])

        self.X_encoded = tokenizer(self.X,max_length=40, truncation=True, padding="max_length", return_tensors="pt")
        self.input_ids = self.X_encoded['input_ids']
        self.attention_mask = self.X_encoded['attention_mask']

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return (self.input_ids[idx], self.attention_mask[idx])
    
    
if __name__ == "__main__":
    from transformers import GPT2Tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    dataset = FinanceDataset("/home/apasalic/workspace/ChatOne/data/new_financial_phrasebank.json", tokenizer)
    print(dataset['rows'][0])