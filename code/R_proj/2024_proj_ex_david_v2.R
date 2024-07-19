set.seed(1950)

n <- 23
r <- 300
m <- 170

samples <- array(dim=c(r, m))

for (i in 1:r){
  for (j in 1:m){
    a <- rnorm(n+1)
    sum_sq <- 0
    
    for (k in a[-1]){
      sum_sq <- sum_sq + k^2
    }
    
    sum_sq <- sqrt(sum_sq)
    
    t <- sqrt(n) * a[1] / sum_sq
    
    samples[i, j] <- t
  }
}


a <- c()
for (i in 1:r){
  menor <- 0
  for (j in 1:m){
    if (samples[i, j] <= 1.5){
      menor <- menor +1
    }
  }
  a[i] <- menor/m
}

aprox = mean(a)

absolute = pt(1.5, n)

abs(aprox -absolute)*100