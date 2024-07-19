# Definir parâmetros
n <- 23
m <- 170
r <- 300
threshold <- 1.5
set.seed(1950)

# Função para calcular T
calculate_T <- function(Z) {
  Z1 <- Z[1]
  Z_rest <- Z[2:(n+1)]
  T <- (sqrt(n) * Z1) / sqrt(sum(Z_rest^2))
  return(T)
}

# Gerar as amostras e calcular proporções
proportions <- numeric(r)
for (i in 1:r) {
  sample <- replicate(m, calculate_T(rnorm(n+1)))
  proportions[i] <- mean(sample <= threshold)
}

# Calcular a média das proporções
p_empirical <- mean(proportions)

# Calcular o valor teórico usando a distribuição t de Student
p_theoretical <- pt(threshold, df=n)

# Calcular a diferença absoluta e multiplicar por 100
difference <- abs(p_empirical - p_theoretical) * 100

# Mostrar os resultados
cat("p_empirical:", p_empirical, "\n")
cat("p_theoretical:", p_theoretical, "\n")
cat("difference * 100:", round(difference, 5), "\n")