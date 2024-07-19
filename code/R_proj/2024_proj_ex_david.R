n <- 23
seed <- 1950 
r <- 300
m <- 170
prob <- 1.5

set.seed(seed)
amostras <- numeric(r)

for (i in 1:r) { # itera por cada amostra
  t_values <- numeric(m) # vetor para armazenar valores t
  for (z in 1:m) { # Calcula os valores de t
    x <- rnorm(n+1) # gera os valores da dist normal
    y <- x[-1] # ignora o Z1
    soma <- sum(y^2) 
    t_values[z] <- sqrt(n) * x[1] / sqrt(soma) 
  }
  amostras[i] <- mean(t_values <= prob) # proporção de t_values <= prob
}

mean_val <- mean(amostras)
prob_2 <- pt(prob, n) # gerador t-student do R

res <- round(abs(mean_val - prob_2) * 100, digits = 5)
print(res)
