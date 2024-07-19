# Create Data
Prop <- c(14, 13, 8, 7, 7, 5, 5, 5)

# Prepare a color palette. Here with R color brewer:
library(RColorBrewer)
myPalette <- brewer.pal(8, "Set2")

# Define the labels with counts
labels <- c("CPCNP", "Carcinoma da Mama", "Fibrose Quística", "Cancro da Próstata",
            "Mieloma Múltiplo", "Elevado RCV e DM | HC", "DM2", "Carcinoma do Esófago")
labels_with_counts <- paste(labels, Prop, sep = " || ")


# Add a title to the pie chart
pie(Prop, 
    labels = labels_with_counts, 
    border = "white", 
    col = myPalette, 
    main = "Indicações Terapêuticas predominantes nos Relatórios Públicos de Avaliação")
    
    
    
