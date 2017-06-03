#!/usr/bin/python

public class RetainBestCache<K, T extends Rankable> {
 
    /* Constructor with a data source (assumed to be slow) and a cache size */
    public RetainBestCache(DataSource<K,T> ds, int entriesToRetain) {
        // Implementation here
    }
 
    /* Gets some data. If possible, retrieves it from cache to be fast. If the data is not cached,
     * retrieves it from the data source. If the cache is full, attempt to cache the returned data,
     * evicting the T with lowest rank among the ones that it has available
     * If there is a tie, the cache may choose any T with lowest rank to evict.
     */
    public T get(K key) {
        // Implementation here
    }
}
 
/*
 * For reference, here are the Rankable and DataSource interfaces.
 * You do not need to implement them, and should not make assumptions
 * about their implementations.
 */
 
public interface Rankable {
    /**
     * Returns the Rank of this object, using some algorithm and potentially
     * the internal state of the Rankable.
     */
    long getRank();
}
 
public interface DataSource<K, T extends Rankable> {
    T get (K key);
}



