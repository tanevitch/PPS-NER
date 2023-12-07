# NER-Inmo

python -m spacy train config.cfg  --output ./output  --paths.train train_data.spacy  --paths.dev test_data.spacy

python -m spacy debug data config.cfg