## Problem Statement

**Building a Lightweight Document-Oriented NoSQL Database System**

The project addresses the need for a simple, file-based NoSQL database that can handle JSON-like document storage with basic database operations, without requiring complex database server setup or external dependencies.

## Key Problems Solved:

### 1. **Simplified Data Persistence**
- Provides a straightforward way to store and retrieve structured data as JSON documents
- Eliminates the complexity of traditional SQL schema design and migrations
- Offers file-based storage that's easy to backup and transport

### 2. **Document-Oriented Data Modeling**
- Allows storing flexible, schema-less documents
- Supports nested objects and arrays within documents
- Enables quick prototyping without fixed table structures

### 3. **Basic Database Operations**
- **CRUD Operations**: Create, Read, Update, Delete documents
- **Querying**: Filter documents based on field values
- **Indexing**: Basic indexing for improved query performance
- **Collection Management**: Organize documents into logical groups

### 4. **Performance Optimization**
- Implements in-memory caching for frequently accessed data
- Provides configurable write strategies (immediate vs. lazy writes)
- Includes basic indexing to speed up common queries

## Core Features Implemented:

- **Database & Collection management**
- **Document CRUD operations**
- **Query filtering with operators** (`=`, `!=`, `>`, `<`, `>=`, `<=`)
- **Basic indexing** on specified fields
- **Data persistence** to JSON files
- **In-memory caching** layer
- **Configurable write strategies**

## Technical Architecture:

```
Database → Collections → Documents
```
- **Database**: Top-level container
- **Collections**: Logical groupings of documents (similar to tables)
- **Documents**: Individual JSON records with unique IDs

## Use Cases:
- **Prototyping applications** needing quick data storage
- **Small to medium projects** where full database servers are overkill
- **Educational purposes** to understand database internals
- **Embedded systems** or environments with limited resources

The project essentially creates a **MongoDB-like lightweight alternative** that can run as a library within applications, providing NoSQL capabilities without external dependencies.
