using API.entities;
using Microsoft.EntityFrameworkCore;

namespace API.data
{
    public class DataContext: DbContext
    {
        public DataContext(DbContextOptions options) : base(options)
        {
        }

        public DbSet<appUser> Users { get; set; }
    }
}