pub fn iterative_fib(n: u64) -> u64 {
    if n == 0 {
        return n;
    }
    let mut last: u64 = 0;
    let mut next: u64 = 1;
    for _ in 1..n {
        let prev_last: u64 = last;
        last = next;
        next = prev_last + next;
    }
    next
}
