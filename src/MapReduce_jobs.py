from pymongo import MongoClient

def get_db_connection():
    client = MongoClient("mongodb://localhost:27017/")
    return client["company_analytics"]

def run_map_reduce_jobs():
    db = get_db_connection()
    
    print('Starting MapReduce jobs...')

    # MapReduce Job 1: Total Profit by Sales Channel
    map_job1 = """
    function() {
        // Emit the sales channel as the key and profit as the value
        emit(this.Channel, this.Profit);
    }
    """
    
    reduce_job1 = """
    function(key, values) {
        // Sum up the profits for each sales channel
        return Array.sum(values);
    }
    """
    # Execute the MapReduce job and store the results in a new collection
    db.command(
        "mapReduce", "orders",
        map=map_job1,
        reduce=reduce_job1,
        out="results_channel_profit"
    )
    print('MapReduce Job 1 completed: Total Profit by Sales Channel')

    # MapReduce Job 2: Total Order Quantity by Region and Product Category
    map_job2 = """
    function() {
        // Emit the region and product category as the key and order quantity as the value
        var key = this.Region + " - " + this["Product Category"];
        emit(key, this["Order Qty"]);
    }
    """
    
    reduce_job2 = """
    function(key, values) {
        // Sum up the order quantities for each region and product category
        return Array.sum(values);
    }
    """
    
    # Execute the MapReduce job and store the results in a new collection
    db.command(
        "mapReduce", "orders",
        map=map_job2,
        reduce=reduce_job2,
        out="results_geo_demand"
    )
    print('MapReduce Job 2 completed: Total Order Quantity by Region and Product Category')
    
    print('MapReduce jobs completed successfully.')

if __name__ == "__main__":
    run_map_reduce_jobs()